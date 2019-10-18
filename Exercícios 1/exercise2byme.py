import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

def legendre(x):
	P = (6435*x**6 - 12012*x**6+6930*x**4-1260*x**2+35 ) / 128
	return P
def funconst(x):
	F = 0*x
	return F
x=np.linspace(-1,1,100)

plt.plot(x,legendre(x),x,funconst(x))
plt.show()

X = [-.5,-.25,.25,.5]
A = []
for i in range(4):
	A.append(newton(legendre, X[i]))
	print(A[i])
