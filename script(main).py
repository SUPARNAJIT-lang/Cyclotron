import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp

# Constants
m = 1.67262192369e-27  # proton mass (kg)
q = 1.602176634e-19    # proton charge (C)

# Lorentz force function
def lorentz(t, y):
    x, y_pos, vx, vy = y
    r = np.sqrt(x**2 + y_pos**2)

    # Magnetic field: only inside radius 3 m
    if r < 3:
        B = np.array([0, 0, 0.01])  # Tesla
    else:
        B = np.array([0, 0, 0])

    # Cyclotron frequency
    w = q / m * np.linalg.norm(B)

    # Electric field: only in narrow D-gap region
    # Use AND instead of OR
    if -0.025 < x < 0.025 and -0.025 < y_pos < 0.025:
        E = np.array([1e5 * np.sin(t * w), 0, 0])  # stronger, realistic field
    else:
        E = np.array([0, 0, 0])

    v = np.array([vx, vy, 0])
    a = (q / m) * (E + np.cross(v, B))
    return [vx, vy, a[0], a[1]]

# Initial conditions
y0 = [0, 0, 0, 0]

# Time span and evaluation points (same as your code)
t_sp = (0, 1e-4)
t_eval = np.linspace(t_sp[0], t_sp[1], 2000)

# Solve ODE
sol = solve_ivp(lorentz, t_sp, y0, t_eval=t_eval, max_step=1e-10)

# Plot trajectory
plt.figure(figsize=(5,5))
plt.plot(sol.y[0], sol.y[1], linewidth=0.8)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Cyclotron Trajectory (x vs y)')
plt.axis('equal')
plt.grid(True)
plt.show()
