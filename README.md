# control_pid_webapp
# 🔧 Control PID WebApp

Proyecto de Innovación Docente, correspondiente a la Convocatoria del Plan AcademiaUGR 2024-25. Código 24-71. Universidad de Granada
Plataforma remota para la resolución y visualización de problemas complejos de ingeniería: control de sistemas.  
La herramienta permite simular sistemas controlados por PID (Proporcional-Integral-Derivativo), enfocada a la enseñanza y experimentación. Permite configurar parámetros PID, visualizar la respuesta de la planta y comprender conceptos como sobreimpulso, tiempo de establecimiento y error en régimen permanente. Fundamentos de Control. 

## 🌐 Características

- Simulación en tiempo real del comportamiento de una planta térmica.
- Interfaz gráfica con control deslizante de consigna y temperatura inicial.
- Visualización en gráfico interactivo (tiempo vs temperatura).
- Evaluación automática del rendimiento del sistema: overshoot, error permanente, etc.
- Botón de parada de simulación para análisis pausado.
- WebSocket bidireccional para comunicación con backend.


## ▶️ Instalación local

Requiere Python 3.9+ y `pip`.

```bash
# Clonar el repositorio
git clone https://github.com/Nubetiza/control_pid_webapp.git
cd control_pid_webapp

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # en Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
uvicorn app.main:app --reload

## 🐳 Despliegue con Docke

# Construir y levantar con docker-compose
docker-compose up --build


## ⚙️ Requisitos
requirements.txt:

css
Copiar
Editar
fastapi
uvicorn[standard]
jinja2
Se recomienda usar uvicorn[standard] para incluir soporte WebSocket con websockets, httptools y otros extras.


# Copyright (c) 2025 Nubetiza - Uso interno exclusivo. No redistribuir.
