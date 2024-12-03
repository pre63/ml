import numpy as np
import matplotlib.pyplot as plt
import sys
from matplotlib.animation import FuncAnimation
from pid import PIDController
from mpc import MPCController


# Base System Class
class System:
  def __init__(self, initial_state=0):
    self.state = initial_state

  def simulate_step(self, state, control_input, dt):
    # For a simple system: dx/dt = u
    return state + control_input * dt

  def update(self, control_input, dt):
    self.state = self.simulate_step(self.state, control_input, dt)
    return self.state

  def reset(self, initial_state=0):
    self.state = initial_state


# RocketSystem Inheriting from System
class RocketSystem(System):
  def __init__(self, position=0.0, velocity=0.0, mass=1000, drag_coefficient=0.1, cross_section_area=1.0):
    super().__init__((position, velocity))  # Initial state is a tuple (position, velocity)
    self.mass = mass
    self.drag_coefficient = drag_coefficient
    self.cross_section_area = cross_section_area
    self.g = 9.81  # Gravity
    self.air_density = 1.225  # Air density

  def simulate_step(self, state, thrust, dt):
    position, velocity = state
    drag = 0.5 * self.air_density * self.drag_coefficient * self.cross_section_area * velocity**2 * np.sign(velocity)
    acceleration = (thrust - drag - self.mass * self.g) / self.mass
    velocity += acceleration * dt
    position += velocity * dt
    return position, velocity

  def reset(self, position=0.0, velocity=0.0):
    self.state = (position, velocity)


def simulate(controllerClass, systemClass):
  # Simulation Parameters
  dt = 0.1
  time_steps = 200
  setpoint = 1000.0 if systemClass == RocketSystem else 1.0  # Target altitude for RocketSystem, default for others

  sim_args = {
      "prediction_horizon": 10,
      "control_horizon": 5,
      "dt": dt,
      "dynamics": None,  # Dynamics handled by system instance
      "cost_function": lambda state, control, setpoint: (state[0] - setpoint) ** 2 + 0.01 * control ** 2
      if isinstance(state, tuple)
      else (state - setpoint) ** 2 + 0.01 * control ** 2,
  }

  controller = controllerClass(**sim_args)

  # System Initialization
  system = systemClass()
  time = np.arange(0, time_steps * dt, dt)
  states = []
  controls = []

  # Simulation Loop
  for t in time:
    current_state = system.state
    control = controller.compute(setpoint, current_state, system)  # Pass system to the controller
    control = max(0, min(control, 20000)) if isinstance(system, RocketSystem) else control
    controls.append(control)
    state = system.update(control, dt)
    states.append(state[0] if isinstance(state, tuple) else state)

  # Visualization with Animation
  fig, ax = plt.subplots()
  ax.set_xlim(0, time_steps * dt)
  ax.set_ylim(0, setpoint * 1.2)
  line, = ax.plot([], [], lw=2, label="State")
  target_line = ax.axhline(y=setpoint, color='r', linestyle='--', label="Target")
  ax.legend()

  def init():
    line.set_data([], [])
    return line,

  def update(frame):
    line.set_data(time[:frame], states[:frame])
    return line,

  ani = FuncAnimation(fig, update, frames=len(time), init_func=init, blit=True, interval=50)
  plt.xlabel("Time (s)")
  plt.ylabel("Altitude (m)" if systemClass == RocketSystem else "State")
  plt.title("Rocket Altitude Control" if systemClass == RocketSystem else "System Control")
  plt.show()


if __name__ == '__main__':
  if len(sys.argv) < 2:
    print("Usage: python script.py <controller> [<simulation>]")
    exit(1)

  param_controller = sys.argv[1]
  param_simulation = sys.argv[2] if len(sys.argv) > 2 else 'rocket'

  controller = None
  simulation = None

  if param_controller == 'pid':
    controller = PIDController
  elif param_controller == 'mpc':
    controller = MPCController
  elif param_controller == 'adaptive':
    print('Adaptive controller not implemented yet')
    exit(1)

  if param_simulation == 'rocket':
    simulation = RocketSystem
  elif param_simulation == 'basic':
    simulation = System
  else:
    print('Invalid simulation parameter')
    exit(1)

  if controller is None or simulation is None:
    print('Invalid controller or simulation parameter')
    exit(1)

  simulate(controller, simulation)
