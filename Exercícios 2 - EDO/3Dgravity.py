from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np 



def G(X,t):

	x,y,z,vx,vy,vz = X
	R = (x**2 + y**2+z**3)**1.5

	dvxdt = - x*R
	dvydt = - y*R
	dvzdt = - z*R
	return [vx,vy,vz, dvxdt, dvydt, dvzdt]

X0 = [20,4,1,3,-2,-1]


t = np.linspace(0,10,1000)
SOL = odeint(G,X0,t)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(SOL[:,0],SOL[:,1],SOL[:,2])
plt.show()

plt.plot(SOL[:,0],SOL[:,1])
plt.show()


def H(X,t):
	m = 2
	k = 1.5
	g = 9.8
	r,theta,phi,Pr,Ptheta, Pphi = X
	Hash = [Pr/m,Ptheta/(r**2*m), Pphi/ (m*r**2 * np.sin(theta)**2), -m*g*np.cos(theta)-k*r, m*g*np.sin(theta)-(Pphi**2*np.cos(theta))/(m*r**2 * np.sin(theta)**3),0]
	return Hash

X0 = [2, .5,2, 1,-2, -1]

tau = np.linspace(0,10,100)
SOLVER = odeint(H,X0,tau)

def Spherical(theta, phi, r):
	#theta, phi = np.linspace(0, 2 * np.pi, 40), np.linspace(0, np.pi, 40)
	THETA, PHI = np.meshgrid(theta, phi)
	R = r
	#R = np.cos(PHI**2)
	X = R * np.sin(PHI) * np.cos(THETA)
	Y = R * np.sin(PHI) * np.sin(THETA)
	Z = R * np.cos(PHI)
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1, projection='3d')
	plot = ax.plot_surface(
    X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('jet'),
    linewidth=0, antialiased=False, alpha=0.5)
	plt.show()