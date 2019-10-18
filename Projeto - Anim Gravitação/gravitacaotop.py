import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
#Dados calculados sobre os planetas

G = 4*np.pi*np.pi
M = 1.0

mu = 4.366244e-5	#Massa de Urano
mn = 5.151389e-5	#Massa de Netuno

du = 19.1914	#Distância de Urano ao Sol
dn = 30.0611	#Distância de Netuno ao Sol

Tur = 84.0110	#Período de Urano
Tnt = 164.7901	#Período de Netuno

omeur = 2*np.pi/Tur		#Velocidade angular de Urano inicial
oment = 2*np.pi/Tnt		#Velocidade angular de Netuno inicial

#Posição de Urano em 1960

radur =  205.64*np.pi/180     #Posição angular de Urano em 1960 em radianos
urx = du*np.cos(radur)          #Posição x de Urano inicial
ury = du*np.sin(radur)	        #Posição y de Urano inicial
velur = omeur*du
velurx = velur*np.sin(radur)	#Velocidade x de Urano inicial
velury = -velur*np.cos(radur)	#Velocidade y de Urano inicial

#Posição de Netuno em 1960	

radnt = 288.38*np.pi/180  #Posição angular de Netuno em 1960
ntx = dn*np.cos(radnt)	    #Posição x de Netuno inicial
nty = dn*np.sin(radnt)      #Posição y de Netuno inicial
velnt = oment*dn
velntx = velnt*np.sin(radnt)	#Velocidade x de Netuno inicial
velnty = -velnt*np.cos(radnt)	#Velocidade y de Netuno inicial
	
x0 = [urx, ury, ntx, nty, velurx, velury, velntx, velnty]  #VALORES INICIAS


def model(x, t):
	urx = x[0]
	ury = x[1]
	ntx = x[2]
	nty = x[3]
	
	Rur = (urx**2 + ury**2)**1.5					#R DE URANO
	Rnt = (ntx**2 + nty**2)**1.5		            #R DE NETUNO
	Rur_nt = ((urx-ntx)**2 + (ury-nty)**2)**1.5		#R ENTRE NETUNO E URANO
	
	Gx = G/Rur_nt*(urx - ntx)
	Gy = G/Rur_nt*(ury - nty)
	Gur = G*M/Rur
	Gnt = G*M/Rnt
	
	vel_urx = x[4]
	vel_ury = x[5]
	vel_ntx = x[6]
	vel_nty = x[7]

	v_ur_xpt = -Gur*urx - mn*Gx
	v_ur_ypt = -Gur*ury - mn*Gy
	v_nt_xpt = -Gnt*ntx + mu*Gx
	v_nt_ypt = -Gnt*nty + mu*Gy

	A = np.array([vel_urx,vel_ury,vel_ntx,vel_nty,v_ur_xpt,v_ur_ypt,v_nt_xpt,v_nt_ypt])
	return A

t = np.arange(0,1000, 0.01)

x = odeint(model, x0, t)

plt.plot(x[:,0], x[:,1], 'g', label = 'Urano')
plt.plot(x[:,2], x[:,3], 'b', label = 'Netuno')
#plt.plot(x[:,4], x[:,5], 'g', label = 'Urano')  #urano
#plt.plot(x[:,6], x[:,7], 'b', label = 'Netuno')  #netuno
plt.legend()
plt.show()


