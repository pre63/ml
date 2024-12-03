import numpy as np


class PIDController:
  def __init__(self, **kwargs):
    self.kp = kwargs.get("kp", 1.0)
    self.ki = kwargs.get("ki", 0.0)
    self.kd = kwargs.get("kd", 0.0)
    self.integral = kwargs.get("integral", 0.0)
    self.previous_error = kwargs.get("previous_error", 0.0)
    self.dt = kwargs.get("dt", 0.1)

  def compute(self, setpoint, measured_value, system):
    # Handle tuple or single-value input
    if isinstance(measured_value, tuple):
      measured_value = measured_value[0]  # Extract position for comparison
    error = setpoint - measured_value
    self.integral += error * self.dt
    derivative = (error - self.previous_error) / self.dt
    self.previous_error = error
    return self.kp * error + self.ki * self.integral + self.kd * derivative
