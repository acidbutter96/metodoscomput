import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from scipy.optimize import newton

plt.rc('text',usetex=True)

hbar = 7.63 #me eV A^2
a = 4 #A
V0 = 16 #eV

m = .9 #Usei me = 1 pois não sei de cabeça qual é a massa do elétron

#item a

def alfa(E):
	al=(2*m*E / hbar)**.5
	return al

def beta(E):
	bet = (2*m*(V0-E) / hbar)**.5
	return bet

#item b

#lado esquerdo equacao

def esquerdopares(x):
	esq = alfa(x)*np.tan(alfa(x)*a)
	return esq

U=np.linspace(0,16,1000)
#lado esquerdo
plt.plot(U,esquerdopares(U),'r',label=r'\alpha \tan (\alpha a)')
#lado direito equacao
plt.plot(U,beta(U),'-.r',label=r'\beta')

#impares

def esquerdoimpares(x):
	esq = alfa(x)*(np.tan(alfa(x)*a))**-1
	return esq

plt.plot(U,esquerdoimpares(U),'b',label=r'\alpha cot (\alpha a)')
plt.plot(U,-beta(U),'-.b',label=r'-\beta')
plt.axis([0,16,-3,3])
plt.xlabel('E')
plt.legend()
plt.show()

#item c

approx = [.4843,.692683, 4.63455, 6.15035, 12.0923]
approxi = [15.9032]

#item d

#interseccoes
def interpar(x):
	return esquerdopares(x)-beta(x)


Raiz = []
for i in range(4):
	Raiz.append(newton(interpar,approx[i]))

for i in range(4):
	print('Energia do Estado ligado')
	print(i+1)
	print(Raiz[i])