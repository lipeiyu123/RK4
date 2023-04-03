

import numpy as np
import matplotlib.pyplot as plt
import math


###
###                     test rk4
###

x = np.array([0,-1,0,1] , dtype=np.float64)     #x y theat v
x3 = np.array([0,-1,0,1] , dtype=np.float64)     #x y theat v

t = 0
dt = 0.1
d_theat = 0.0001

x_list = []
y_list = []
x3_list = []
y3_list = []

x_list.append(x[0])
y_list.append(x[1])
x3_list.append(x3[0])
y3_list.append(x3[1])

def Fun( input , other):
        out = np.zeros(4)
        out[0] = input[3] * math.cos(input[2])
        out[1] = input[3] * math.sin(input[2])
        out[2] = other
        out[3] = 0  
        return out
def RK4(Fun , input , other):
        k1 = Fun(input , other)
        k2 = Fun(input + 0.5*dt*k1 , other)
        k3 = Fun(input + 0.5*dt*k2 , other)
        k4 = Fun(input + dt*k2 , other)
        input = input + (k1 + 2*k2 + 2*k3 + k4) * dt / 6
        return input


for i in range(int(2* math.pi / d_theat)):
        t += dt
        fun = Fun
        x = RK4(fun , x , d_theat)

        x3[0] = x3[3] * math.sin(x3[2]) / d_theat
        x3[1] = -x3[3]* math.cos(x3[2]) /d_theat + (1/d_theat -1)
        x3[2] = t * d_theat

        x_list.append(x[0])
        y_list.append(x[1])

        x3_list.append(x3[0])
        y3_list.append(x3[1])

plt.plot(x_list,y_list , '-*r')
plt.plot(x3_list,y3_list , '-*b')
plt.show()
        