import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def dydt(y,t):
	if t<10:
		u = .0
	else:
		u = 2.0
	return (-y+u)/5

y0 = 1

t = np.linspace(0,20,100)

y = odeint(dydt,y0,t)

#plt.plot(t,y,label='Exercise 2')
#plt.xlabel('t')
#plt.ylabel('x')
#plt.show()


#EDO SEGUNDA ORDEM - MHS

v00 = 2
y00 = 1
def ddotx(x,t):
	return -x

def dotx(ddx,t):
	return odeint(ddotx,v00,t)

ysol = odeint(dotx,y00,t)

plt.plot(t,ysol)