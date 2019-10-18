import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#def dfdt(x,t,mu):
#	dxdt = mu*np.cos(mu*x)
#	return dxdt


#X0 = []
#t = np.linspace(0,.5,1000)

#SOL = []
#for j in range(2):
#	X0.append(.5*j*(-1)**(-j))
#	SOL.append(odeint(dfdt, .02, t, args=(-20+j,)))
#	plt.plot(t, SOL[j])

#plt.show()

def G(X,t):  #X = [x, y, vx, vy]
	x = X[0]
	y = X[1]
	m1 = 1
	m2 = 20
	R = (X[0]**2+X[1]**2)**1.5
	dvxdt = - (X[0]*m1*m2 )/ R
	dvydt = -(X[1]*m1*m2)/ R

	return [X[2], X[3], dvxdt, dvydt] 

X0 = [-2, -1, 4, 1]



t= np.linspace(0,500,100000)
SOL = odeint(G, X0, t)

plt.plot(SOL[:,0],SOL[:,1])
plt.show()