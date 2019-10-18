from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

#def Vanderpol(X,t):
#	mu = .5
#	x = X[0]
#	v = X[1]
#	dvdt = -x - mu*(x**2 - 1)*v
#	return [v, dvdt]
#
#X0 = [.5, 2]
#t=np.linspace(0,8*np.pi,2000)
#solve = odeint(Vanderpol, X0, t)

#plt.plot(solve[:,0],solve[:,1],t,solve[:,1])
#plt.show()


def Vanderpol(X,t,mu):
	x = X[0]
	v = X[1]

	dvdt = -x - mu*(x**2 - 1)*v
	return [v, dvdt]

X0 = []
SOL = []
Mu = []
t=np.linspace(0,8*np.pi,20000)
for i in range(500):
	Mu.append(i*.5) #COEFICIENTE

for i in range(20):
	X0.append([.5+i*.5,0])
	for j in range(10):
		SOL.append(odeint(Vanderpol, X0[i],t,args=(Mu[j],)))
	plt.figure(1)
	plt.subplot(211)
	plt.plot(t,SOL[i][:,0])

	plt.subplot(212)
	plt.plot(SOL[i][:,0], SOL[i][:,1])
#solve = odeint(Vanderpol, X0, t)

#plt.plot(solve[:,0],solve[:,1],t,solve[:,1])
plt.show()
