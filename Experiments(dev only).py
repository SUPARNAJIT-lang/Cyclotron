import numpy as np
from matplotlib import pyplot as plt

from scipy.integrate import solve_ivp

m=1.67262192369*(10**-27)
q=1.602176634*(10**-19)



def lorentz(t,y):
    x, y_pos, vx, vy = y
    r = np.sqrt(x ** 2 + y_pos ** 2)

    if r<0.04 :
        B = np.array([0, 0, 1])
        w = (q / m) * float(np.linalg.norm(B))
    else:
        B = np.array([0, 0, 0])
        w = (q / m) * float(np.linalg.norm(B))


    if -0.001<x<0.001 and -0.04<y_pos<0.04:
        E = np.array([((10**6) * np.sign(np.sin(t * w))), 0, 0])
    else:
        E=np.array([0,0,0])

    v=np.array([vx,vy,0])
    a=(q/m)*(E+np.cross(B,v))

    return [vx,vy,a[0],a[1]]
print("Your simulation is running")
y0=[0,0,0,0]

t_sp=(0,10**-6)
t_eval=np.linspace(t_sp[0],t_sp[1],20000)

sol1=solve_ivp(lorentz,t_sp,y0,t_eval=t_eval,max_step=(10**-10))





plt.figure(figsize=(5,5))

plt.plot(sol1.y[0], sol1.y[1],linewidth=0.8)
plt.xlabel('x (m)'); plt.ylabel('y (m)')
plt.title('Trajectory (x vs y)')
plt.axis('equal')
plt.grid(True)
plt.show()

k=0.5*m*((sol1.y[2]**2)+(sol1.y[3]**2))


plt.plot(t_eval,k)
plt.xlabel('Time (t)'); plt.ylabel('Kinetic Energy (J)')
plt.title('Kinetic Energy vs Time')
plt.grid(True)
plt.show()