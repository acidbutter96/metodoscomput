import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, bisect
import math as m


def Legendre(x):
	P = (6435*x**8-12012*x**6+ 6930 * x**4 - 1260 * x**2 + 35 ) / 128
	return P

def f(x):
	f = 0*x
	return f

x = np.linspace(-1,1,1000)

plt.plot(x, Legendre(x), x, f(x))
plt.show()


X0 = [-.987973, -.767046, -.479423, -.162621, .166686, .491824, .775278, .987869]
Y0 = []
for i in range(8):
	Y0.append(newton(Legendre, X0[i]))

print(Y0)

resultado=[]
for j in range(8):
	if np.abs(f(Y0[j])) != 0:
		resultado.append('true')
	else:
		resultado.append('false')
