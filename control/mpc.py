import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.optimize import minimize


def cost_function(state, control, setpoint):
  position = state[0] if isinstance(state, tuple) else state
  state_cost = ((position - setpoint) / setpoint) ** 2  # Normalized state cost
  control_cost = (control / 20000) ** 2  # Normalize thrust to its max bound
  return state_cost + 0.01 * control_cost


from scipy.optimize import minimize
import numpy as np


class MPCController:
  def __init__(self, **kwargs):
    self.prediction_horizon = kwargs.get("prediction_horizon", 10)
    self.control_horizon = kwargs.get("control_horizon", 5)
    self.dt = kwargs.get("dt", 0.1)
    self.cost_function = kwargs.get(
        "cost_function",
        lambda state, control, setpoint: ((state[0] - setpoint) / setpoint) ** 2 + 0.01 * (control / 20000) ** 2,
    )
    self.bounds = kwargs.get("bounds", [(0, 20000) for _ in range(self.control_horizon)])
    self.initial_guess = kwargs.get("initial_guess", np.ones(self.control_horizon) * 10000)  # Mid-thrust

  def compute(self, setpoint, current_state, system):
    def optimization_function(control_sequence):
      state = current_state
      cost = 0.0
      for u in control_sequence:
        state = system.simulate_step(state, u, self.dt)
        if isinstance(state, tuple) and state[0] < 0:  # Penalize negative altitude
          cost += 1e6
        cost += self.cost_function(state, u, setpoint)
      return cost

    # Run optimization
    result = minimize(
        optimization_function,
        self.initial_guess,
        bounds=self.bounds,
        method="L-BFGS-B",
        options={"maxiter": 100, "ftol": 1e-4},
    )

    if not result.success:
      print(f"Optimization failed: {result.message}")
      return self.initial_guess[0]  # Return the first guess to maintain continuity

    return result.x[0]  # Apply the first control input
