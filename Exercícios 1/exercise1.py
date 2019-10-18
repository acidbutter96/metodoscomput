from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def vanderpol(X,t,mu):
	x = X[0]
	y = X[1]
	dxdt = mu * (x - (1/3)*x**3 - y)+4*np.cos(5*t)
	dydt = x / mu
	return [dxdt,dydt]
X0 = [1, 2]
t = np.linspace(0,80*np.pi,2500)

#ol = odeint(vanderpol, X0, t)

#x = sol[:,0]
#y = sol[:,1]

MU = [ ]
SOL = [ ]
for i in range(1):
	MU.append(i*.01+.5)

for i in range(1):
	SOL.append(odeint(vanderpol, X0, t, args=(MU[i],)))
for i in range(1):
	#plt.plot(t,SOL[i][:,0], t,SOL[i][:,1])
	plt.plot(SOL[i][:,0],SOL[i][:,1])
#plt.plot(x,y)
plt.show()