from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

l = 6 #metter
g = 9.8 #metter per second
def osc(X,t):
	theta = X[0]
	w = X[1]
	dwdtheta = -(g / l / w)*np.sin(theta)
	return [w, dwdtheta]


osc0 = [10, 1]

t = np.linspace(0,100,1000)

y1 = odeint(osc, osc0, t)

plt.plot(y1[:,0], y1[:,1])
plt.show()