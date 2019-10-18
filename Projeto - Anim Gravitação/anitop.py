import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import odeint

np.random.seed(19680801)

# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)


def path_generator(steps, step):
	path = np.empty((3, steps))
	for i in range(1, steps):
		x_ran, y_ran, z_ran = np.random.rand(3)
		sgnX = (x_ran - 0.5)/abs(x_ran - 0.5)
		sgnY = (y_ran - 0.5)/abs(y_ran - 0.5)
		sgnZ = (z_ran - 0.5)/abs(z_ran - 0.5)
		dis = np.array([step*sgnX, step*sgnY, step*sgnZ])
		path[:, i] = path[:, i - 1] + dis

	return path		

def random_walk_3D_animated(n, traj = 1):

	fig = plt.figure()
	ax = p3.Axes3D(fig)

	particles = [path_generator(n, 1) for i in range(traj)]
	trajectories = [ax.plot(particle[0, 0:1], particle[1, 0:1], particle[2,0:1],'og')[0] for particle in particles]

	ax.set_xlim3d([-100, 100])
	ax.set_ylim3d([-100, 100])
	ax.set_zlim3d([-100, 100])

	for add in np.arange(traj):
		ims.append(trajectories[i])
	animacion = animation.FuncAnimation(fig, animate, 1000, interval=50,blit=False)
	animacion.save('random.mp4',writer=writer)
	plt.show()



def osc(X,t):
	w = 10
	x,vx=X
	dvxdt = -w*x
	#dvydt = -w*y
	#dvzdt = -w*z
	return [vx,dvxdt]

fig3 = plt.figure()

X0=[10,-2]
t = np.arange(0,150,.1)
U = odeint(osc,X0,t)

def oscforc(t):
	F0 = 10
	beta = .4
	w = .1
	w0 = 3
	x = F0 *((w0**2-w**2)**2+(2*beta*w)**2)**-.5 *np.cos(w*t)+np.exp(-2*beta*t)*np.cos(w0*t)
	return x
U1 = oscforc(t)

def t(num):
	return np.arange(0,num,.1)
ims = []
#for i in np.arange(15):
#	plt.plot(U[,0],U[i,1])
#	plt.show()

for add in np.arange(150):
	plt.legend()
	ims.append((plt.plot(t(add),oscforc(t(add)),'r')))

im_ani = animation.ArtistAnimation(fig3, ims, interval = 50, repeat_delay=3000, blit=True)
im_ani.save('osc.mp4',writer=writer)