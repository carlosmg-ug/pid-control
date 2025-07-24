from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from app.simuladores import PlantaNivel, PID
import asyncio
from app.config_profesor import R_PLANTA, C_PLANTA, ERROR_PERMITIDO, TIEMPO_ESTABLECIDO
from app.config_profesor import (
    PRACTICA2_R_PLANTA,
    PRACTICA2_C_PLANTA,
    PRACTICA2_TAU_RETARDO,
    PRACTICA2_GANANCIA,
    PRACTICA2_ERROR_PERMITIDO,
    PRACTICA2_TIEMPO_ESTABLECIDO,
)

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



@app.get("/practica/pid", response_class=HTMLResponse)
async def pid_page(request: Request):
    return templates.TemplateResponse("practica1.html", {
        "request": request,
        "r_planta": R_PLANTA,
        "c_planta": C_PLANTA,
        "error_permitido": ERROR_PERMITIDO,
        "tiempo_establecido": TIEMPO_ESTABLECIDO
    })

@app.get("/practica/temp", response_class=HTMLResponse)
async def temp_page(request: Request):
    return templates.TemplateResponse("practica2.html", {
        "request": request,
        "r_planta": PRACTICA2_R_PLANTA,
        "c_planta": PRACTICA2_C_PLANTA,
        "retardo": PRACTICA2_TAU_RETARDO,
        "ganancia": PRACTICA2_GANANCIA,
        "error_permitido_temp": PRACTICA2_ERROR_PERMITIDO,
        "tiempo_establecido_temp": PRACTICA2_TIEMPO_ESTABLECIDO
    })

    
    
@app.websocket("/ws/pid")
async def websocket_pid(ws: WebSocket):
    await ws.accept()
    print("✅ WebSocket aceptado.")

    planta = None
    pid = None
    nivel_inicial = 0.0

    while True:
        try:
            data = await ws.receive_json()
            if data.get("iniciar"):
                kp = float(data.get("kp"))
                ki = float(data.get("ki"))
                kd = float(data.get("kd"))
                setpoint = float(data.get("setpoint"))
                nivel_inicial = float(data.get("nivel_inicial", 0))

                await ws.send_json({
                    "config": {
                        "error_permitido": ERROR_PERMITIDO,
                        "tiempo_establecido": TIEMPO_ESTABLECIDO
                    }
                })
                
                planta = PlantaNivel(R=R_PLANTA, C=C_PLANTA)
                planta.h = nivel_inicial
                pid = PID(kp=kp, ki=ki, kd=kd, dt=0.1, setpoint=setpoint)

            if planta and pid:
                planta.q_in = pid.calcular(planta.h)
                h = planta.paso(0.1)
                await ws.send_json({"nivel": round(h, 2)})

        except Exception as e:
            print(f"[WebSocket cerrado] {e}")
            break


@app.websocket("/ws/temp")
async def websocket_temp(websocket: WebSocket):
    await websocket.accept()

    data = await websocket.receive_json()
    if "iniciar" not in data:
        await websocket.close()
        return

    await websocket.send_json({
        "config": {
            "error_permitido": PRACTICA2_ERROR_PERMITIDO,
            "tiempo_establecido": PRACTICA2_TIEMPO_ESTABLECIDO
        }
    })

    temperatura = data["temperatura_inicial"]
    setpoint = data["setpoint"]
    kp = data["kp"]
    ki = data["ki"]
    kd = data["kd"]

    error_acumulado = 0
    error_anterior = 0
    dt = 0.1
    retardo_buffer = [0] * int(PRACTICA2_TAU_RETARDO / dt)  # buffer para simular retardo

    while True:
        try:
            await websocket.receive_text()  # esperar ping

            # Control PID
            error = setpoint - temperatura
            error_acumulado += error * dt
            derivada = (error - error_anterior) / dt
            error_anterior = error

            control = kp * error + ki * error_acumulado + kd * derivada

            # Aplicar retardo
            retardo_buffer.append(control)
            control_con_retardo = retardo_buffer.pop(0)

            # Modelo térmico con retardo y ganancia
            dTemperatura = (1 / (PRACTICA2_R_PLANTA * PRACTICA2_C_PLANTA)) * \
                (PRACTICA2_R_PLANTA * PRACTICA2_GANANCIA * control_con_retardo - temperatura)
            temperatura += dTemperatura * dt

            await websocket.send_json({
                "temperatura": round(temperatura, 3)
            })

            await asyncio.sleep(dt)

        except Exception:
            break
