"""
   PRACTICA 1  
    
🧠 Interpretación de los parámetros:
🔵 h(t)
Nivel de líquido en el tanque (en milímetros o cm, según cómo lo definas tú).

🔵 q_i(t)
Caudal de entrada (en L/min, cm³/s, etc.). Es la señal de entrada que el PID controla.

🔴 C: Capacidad del sistema (constante de almacenamiento)
Equivale al área transversal del tanque si supones que el caudal de entrada/salida afecta directamente a la altura.

Unidad típica: litros por milímetro (L/mm) o cm³/mm si la altura es en mm.

Ejemplo:
Si C = 5.0 significa que por cada 5 unidades de entrada neta, el nivel sube 1 mm.

🔴 R: Resistencia hidráulica del sistema (constante de salida)
Representa qué tan difícil es que el líquido salga del tanque. Es análogo a una resistencia eléctrica.

Se relaciona con el estrechamiento del orificio de salida o del tubo de desagüe.

Unidad típica: segundos / litro, o s·mm/cm³.

Ejemplo:
Si R = 2.0, significa que si el nivel del tanque es 10 mm, el flujo de salida será 5 unidades (10 / 2).
    
    
🛠️ En tu simulación:

Un C alto hace que el tanque suba más lento.

Un R alto hace que el tanque se vacíe más lentamente (menos flujo de salida para una misma altura).


"""

R_PLANTA = 2
C_PLANTA = 4

# Parámetros de estabilización
ERROR_PERMITIDO = 0.5     # en mm
TIEMPO_ESTABLECIDO = 2.0  # en segundos







# ================================
# CONFIGURACIÓN PRÁCTICA 2: CONTROL DE TEMPERATURA
# ================================

# Parámetros físicos del modelo térmico

# PRACTICA2_R_PLANTA: Resistencia térmica (°C/W)
# Representa la dificultad con la que el calor fluye desde el sistema al ambiente.
# Cuanto mayor es este valor, más lentamente se disipa el calor hacia el entorno.
PRACTICA2_R_PLANTA = 10.0

# PRACTICA2_C_PLANTA: Capacidad térmica (J/°C)
# Es una medida de cuánta energía necesita el sistema para cambiar su temperatura.
# A mayor capacidad térmica, más lentamente cambia la temperatura ante una entrada de energía.
PRACTICA2_C_PLANTA = 2.0

# PRACTICA2_TAU_RETARDO: Retardo de transporte térmico (s)
# Este valor simula el retraso temporal entre la aplicación de la energía térmica
# (por ejemplo, desde una resistencia o ventilador) y su efecto sobre la temperatura medida.
# Es típico en sistemas reales donde hay inercia o distancia entre sensor y fuente de calor.
PRACTICA2_TAU_RETARDO = 1.5

# PRACTICA2_GANANCIA: Ganancia del sistema
# Escala el efecto que tiene una entrada de energía sobre el cambio de temperatura.
# Puede incluir efectos combinados de resistencia del ventilador, eficiencia del calor, etc.
PRACTICA2_GANANCIA = 1

# ================================
# CRITERIOS DE ESTABILIZACIÓN
# ================================

# PRACTICA2_ERROR_PERMITIDO: Margen de error admisible (°C)
# Define cuánto puede alejarse la temperatura real de la consigna para considerarse estabilizado.
# Ejemplo: si la consigna es 40 °C y este valor es 1.5 °C, se aceptan valores entre 38.5 °C y 41.5 °C.
PRACTICA2_ERROR_PERMITIDO = 5

# PRACTICA2_TIEMPO_ESTABLECIDO: Tiempo de permanencia estable (s)
# Es el tiempo consecutivo que la planta debe permanecer dentro del margen de error para considerarse "estabilizada".
# Este criterio ayuda a evitar falsas estabilizaciones por oscilaciones puntuales.
PRACTICA2_TIEMPO_ESTABLECIDO = 5.0
