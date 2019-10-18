import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def G(X,t,mu):
	x = X[0]
	v = X[1]
	dvdt=-x-mu*(x**2-1)*v
	return [v,dvdt]

X01 = []
X02 = []

SOLU = []
SOLU2 = []

sols = 13
mus = 13
t=np.linspace(0,10,1000)


def EDO(X,t):
	l, g, ay, ax = 3,9.8,10,10
	theta, dtheta = X
	ddtheta = (g + ay)/l*np.sin(theta)- ax/l*np.cos(theta)
	return [dtheta, ddtheta]

E0 = [3,2]

U = odeint(EDO,E0, t)
plt.plot(t,U[:,0])
plt.show()

#for i in range(sols):
#	X01.append([0,.5*i+.5])
#	X02.append([.5+.5*i,0])

#for j in range(0,sols):
#	for k in range(0,mus):
#		SOLU.append(odeint(G,X01[j],t,args=(.1*k,)))
#		SOLU2.append(odeint(G,X02[j],t,args=(.1*k,)))
#	plt.subplot(221)
#	plt.plot(t,SOLU[j][:,0],t,SOLU2[j][:,0],label=j)

#for j in range(0,sols):
#	for k in range(0,mus):
#		SOLU.append(odeint(G,X01[j],t,args=(.1*k,)))
#		SOLU2.append(odeint(G,X02[j],t,args=(.1*k,)))
#	plt.subplot(222)
#	plt.title('Velocidades variadas')
#	plt.plot(t,SOLU[j][:,1],t,SOLU2[j][:,1],label=j)

#for j in range(0,sols):
#	for k in range(0,mus):
#		SOLU.append(odeint(G,X01[j],t,args=(.1*k,)))
#		SOLU2.append(odeint(G,X02[j],t,args=(.1*k,)))
#	plt.subplot(223)
#	plt.title('Diagrama de fases variação na velocidade')
#	plt.plot(SOLU[j][:,0],SOLU[j][:,1],label=j)

#for j in range(0,sols):
#	for k in range(0,mus):
#		SOLU.append(odeint(G,X01[j],t,args=(.1*k,)))
#		SOLU2.append(odeint(G,X02[j],t,args=(.1*k,)))
#	plt.subplot(224)
#	plt.title('Diagrama de fases variação na posição')
#	plt.plot(SOLU2[j][:,0],SOLU2[j][:,1],label=j)




plt.show()

def exeplot(G,t,steps,steps1,mus,sols):
	Sts1 = steps1
	Sts = steps
	X01 = []
	X02 = []

	SOLU = []
	SOLU2 = []



	for i in range(sols):
		X01.append([0,Sts1*i+Sts1])
		X02.append([Sts1+Sts1*i,0])

	for j in range(0,sols):
		for k in range(0,mus):
			SOLU.append(odeint(G,X01[j],t,args=(Sts*k,)))
			SOLU2.append(odeint(G,X02[j],t,args=(Sts*k,)))
		plt.subplot(221)
		plt.plot(t,SOLU[j][:,0],t,SOLU2[j][:,0],label=j)

	for j in range(0,sols):
		for k in range(0,mus):
			SOLU.append(odeint(G,X01[j],t,args=(Sts*k,)))
			SOLU2.append(odeint(G,X02[j],t,args=(Sts*k,)))
		plt.subplot(222)
		plt.title('Velocidades variadas')
		plt.plot(t,SOLU[j][:,1],t,SOLU2[j][:,1],label=j)

	for j in range(0,sols):
		for k in range(0,mus):
			SOLU.append(odeint(G,X01[j],t,args=(Sts*k,)))
			SOLU2.append(odeint(G,X02[j],t,args=(Sts*k,)))
		plt.subplot(223)
		plt.title('Diagrama de fases variação na velocidade')
		plt.plot(SOLU[j][:,0],SOLU[j][:,1],label=j)

	for j in range(0,sols):
		for k in range(0,mus):
			SOLU.append(odeint(G,X01[j],t,args=(.1*k,)))
			SOLU2.append(odeint(G,X02[j],t,args=(.1*k,)))
		plt.subplot(224)
		plt.title('Diagrama de fases variação na posição')
		plt.plot(SOLU2[j][:,0],SOLU2[j][:,1],label=j)
	plt.show()



def F(X,t,w):
	x = X[0]
	v = X[1]
	dvdt = w*np.exp(v)
	return [v,dvdt]