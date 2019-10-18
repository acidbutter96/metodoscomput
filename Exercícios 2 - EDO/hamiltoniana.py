import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
#from matplotlib import animation
#from matplotlib.animation import FuncAnimation,FFMpegFileWriter
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
#import matplotlib.animation as animation


#from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
#rc('text', usetex=True)

# Set up formatting for the movie files
#Writer = animation.writers['ffmpeg']
#writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

#plt.rc('text', usetex=True)
#plt.rc('font', family='serif')

def H(X,t):
	m = 13
	b = 1
	g = 9.8
	r = X[0]
	k = 2
	phi = X[1]
	Pr = X[2]
	Pphi = X[3]

	DHDphi = m*g*r*np.sin(phi)	#momento de phi
	DHDPphi = Pphi/(r**2*m) 	#phi ponto

	DHDr = -k*(r-b)	#forca de r
	DHDPr = Pr / m
	return [Pr, Pphi, DHDr, DHDphi]

X0 = [3, 6, 10, 20]

t = np.linspace(0,30,1000)
SOL = odeint(H,X0,t)

plt.subplot(221)
plt.xlabel(r't')
plt.ylabel(r'r')
plt.plot(t,SOL[:,0])


plt.subplot(222)
plt.xlabel(r't')
plt.ylabel(r'\phi')
plt.plot(t,SOL[:,1])


plt.subplot(223)
plt.xlabel(r't')
plt.ylabel(r'p_{r}')
plt.plot(t,SOL[:,2])


plt.subplot(224)
plt.xlabel(r't')
plt.ylabel(r'p_{\phi}')
plt.plot(t,SOL[:,3])
plt.show()

US = []


def manys(u,t):
	SOLS = []
	
	for i in range(u):
		for j in range(u):
			for k in range(u):
				US.append([.5*i,.5*(j),.5*(j+i),.5*(j-i)])


	for i in range(u**3):
		SOLS.append(odeint(H,US[i],t))

		plt.subplot(221)
		plt.xlabel(r't')
		plt.ylabel(r'r')
		plt.plot(t,SOLS[i][:,0])


		plt.subplot(222)
		plt.xlabel(r't')
		plt.ylabel(r'\phi')
		plt.plot(t,SOLS[i][:,1])


		plt.subplot(223)
		plt.xlabel(r't')
		plt.ylabel(r'p_{r}')
		plt.plot(t,SOLS[i][:,2])


		plt.subplot(224)
		plt.xlabel(r't')
		plt.ylabel(r'p_{\phi}')
		plt.plot(t,SOLS[i][:,3])
	plt.show()


def manyspolar(u,t):
	SOLS = []
	
	for i in range(u):
		for j in range(u):
			for k in range(u):
				US.append([.5*i,.5*(j),.5*(j+i),.5*(j-i)])


	for i in range(u**3):
		SOLS.append(odeint(H,US[i],t))

		plt.polar(SOLS[i][:,0],SOLS[i][:,1])
	plt.show()


plt.show()

t = np.linspace(0,5,1000)
u = 2
for i in range(u):
	SUP = odeint(H,[i**i,2*i,i-2,i+4],t)
	R = SUP[:,0]
	theta = SUP[:,1]
	Xx = R*np.cos(theta)
	Yy = R*np.sin(theta)
	plt.plot(Xx,Yy)
plt.show()

tzao = np.linspace(0,100,1e6)
PHASIS = odeint(H,[-13,-20*np.pi,80,-45],tzao)
#plt.subplot(211)
#plt.plot(PHASIS[:,0],PHASIS[:,2])
#plt.subplot(212)
plt.plot(PHASIS[:,1],PHASIS[:,3],'r')
plt.show()


for i in range(100):
	PHASIS = odeint(H,[-13,0,-20,2],np.linspace(0,i+.1,1000))
	plt.plot(PHASIS[:,1],PHASIS[:,3])
	plt.savefig('phasis.png')
#	plt.axis([])
	
fig2 = plt.figure()