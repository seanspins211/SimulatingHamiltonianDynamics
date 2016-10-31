# Forward Euler for LJ potential
import numpy as np
import matplotlib.pyplot as plt
dt  = 0.00001
q_n  = 1.9
v_n = 0
E_0 = (v_n**2/2) + q_n**(-12)-2*q_n**(-6)

t = np.arange(0,100,dt)
q = np.zeros_like(t)
v = np.zeros_like(t)
E = np.zeros_like(t)

q[0] = q_n
v[0] = v_n
E[0] = 0

for i in range(len(t)-1):

    q_np1 = q_n + dt*v_n
    v_np1 = v_n + 12*dt*(q_n**(-13)-q_n**(-7))
    q_n = q_np1
    v_n = v_np1
    q[i+1] = q_n
    v[i+1] = v_n
    E[i+1] = (E_0-((v_n**2)/2 + q_n**(-12)-2*q_n**(-6)))/E_0



plt.plot(q,v)
plt.show()
plt.plot(t,E)
plt.show()
