import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(y,t,k):
	dydt = -k * y
	return dydt


def dydt(y,t):
	if t<10:
		u = .0
	else:
		u = 2.0
	return (-y+u)/5


#derivatives


y0 = 2

#initial conditions

t = np.linspace(-10,20,300)

#y = odeint(model,y0,t)

Ks = [ ]
SOL = [ ]


for i in range(60):
	Ks.append(i*.2+1)

for k in range(60):
	SOL.append(odeint(model,5,t,args=(Ks[k],)))
for j in range(60):
	plt.plot(t,SOL[j])

plt.show()