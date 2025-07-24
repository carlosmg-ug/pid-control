class PlantaNivel:
    def __init__(self, R=2.0, C=5.0):
        self.R = R
        self.C = C
        self.h = 0.0
        self.q_in = 0.0

    def paso(self, dt):
        q_out = self.h / self.R
        dh = (self.q_in - q_out) / self.C * dt
        self.h = max(0.0, self.h + dh)
        return self.h

class PID:
    def __init__(self, kp, ki, kd, dt, setpoint):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.dt = dt
        self.setpoint = setpoint
        self.integral = 0
        self.last_error = 0

    def calcular(self, h_actual):
        error = self.setpoint - h_actual
        self.integral += error * self.dt
        d_error = (error - self.last_error) / self.dt
        self.last_error = error
        output = self.kp * error + self.ki * self.integral + self.kd * d_error
        return max(0.0, output)
