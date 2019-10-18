import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


#item a

def Lorentz(X,t):
	alfa = 10
	beta = 8 / 3
	rho = 28
	x,y,z = X
	dxdt = alfa*(y-x)
	dydt = x*(rho-z)-y
	dzdt = x*y-beta*z
	return [dxdt,dydt,dzdt]
X0 = [-10,-10,30]


t = np.linspace(0,20,2000)

SOL = odeint(Lorentz, X0,t)


plt.plot(t,SOL[:,0],'b',label='x')
plt.plot(t,SOL[:,1],'orange',label='y')
plt.plot(t,SOL[:,2],'g',label='z')
plt.xlabel('t')
plt.legend()
plt.show()

plt.plot(SOL[:,0],SOL[:,2],label='x e z')
plt.legend()
plt.xlabel('x')
plt.ylabel('z')

plt.show()