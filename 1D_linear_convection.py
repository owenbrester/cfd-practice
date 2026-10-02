"""
The simplest CFD problem
 
    du/dt + c * du/dx = 0
"""
 
import numpy as np
import matplotlib.pyplot as plt
 
nx = 41                  # number of grid points
dx = 2 / (nx - 1)        # distance between grid points
nt = 25                  # number of timesteps
dt = 0.025               # size of each timestep
c = 1                    # wave speed
 
# u = 2 between x=0.5 and x=1, u = 1 everywhere else.
u = np.ones(nx)
u[int(0.5 / dx):int(1 / dx + 1)] = 2
 
u_initial = u.copy()  # copy to compare later
 
# At each timestep, compute the new value of u at every grid point using a finite-difference approximation of du/dt + c*du/dx = 0.
# Rearranged: u_new[i] = u[i] - c * dt/dx * (u[i] - u[i-1])
for n in range(nt):
    un = u.copy()
    for i in range(1, nx):
        u[i] = un[i] - c * dt / dx * (un[i] - un[i - 1])
 
x = np.linspace(0, 2, nx)
plt.plot(x, u_initial, label="initial (t=0)", linestyle="--")
plt.plot(x, u, label=f"after {nt} steps")
plt.xlabel("x")
plt.ylabel("u")
plt.title("1D Linear Convection")
plt.legend()
plt.grid(True)
plt.show()
 