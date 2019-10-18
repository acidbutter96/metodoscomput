import numpy as np
from scipy.integrate import odeint
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)


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
	urx, ury, urz, ntx, nty, ntz, vel_urx, vel_ury,vel_urz, vel_ntx, vel_nty, vel_ntz = x
	
	Rur = (urx**2 + ury**2=urz**2)**1.5					#R DE URANO
	Rnt = (ntx**2 + nty**2=ntz**2)**1.5		            #R DE NETUNO
	Rur_nt = ((urx-ntx)**2 + (ury-nty)**2+(urz-ntz)**2)**1.5		#R ENTRE NETUNO E URANO
	
	Gx = G/Rur_nt*(urx - ntx)
	Gy = G/Rur_nt*(ury - nty)
	Gz = G/Rur_nt*(urz - ntz)
	Gur = G*M/Rur
	Gnt = G*M/Rnt
	
	v_ur_xpt = -Gur*urx - mn*Gx
	v_ur_ypt = -Gur*ury - mn*Gy
	v_ur_zpt = -Gur*urz - mn*Gz
	v_nt_xpt = -Gnt*ntx + mu*Gx
	v_nt_ypt = -Gnt*nty + mu*Gy
	v_nt_zpt = -Gnt*ntz + mu*Gz
	A = np.array([vel_urx,vel_ury,vel_urz,vel_ntx,vel_nty,vel_ntz,v_ur_xpt,v_ur_ypt,v_ur_xpt,v_nt_xpt,v_nt_ypt,v_nt_zpt])
	return A

t = np.arange(0,1000, 1)
x = odeint(model,x0,t)

def resolve(t):
	return odeint(model, x0, t)

def tadd(add):
	return np.arange(0,add,1)
fig0 = plt.figure()
plt.plot(x[:,0], x[:,1], 'og', label = 'Urano')
plt.plot(x[:,2], x[:,3], 'ob', label = 'Netuno')
#plt.plot(x[:,4], x[:,5], 'g', label = 'Urano')  #urano
#plt.plot(x[:,6], x[:,7], 'b', label = 'Netuno')  #netuno
plt.legend()
plt.show()

ims = []
fig = plt.figure()
#U = resolve(t)
for add in np.arange(10):
	ims.append((plt.plot(x[add,0],x[add,1],'og', x[add,2],x[add,3],'ob', [0],[0], 'oy')))
	plt.legend()

im_ani = animation.ArtistAnimation(fig, ims, interval = 50, repeat_delay=300, blit=True)
im_ani.save('gravit.mp4',writer=writer)

fig2 = plt.figure()

ims2 = []

for add in np.arange(1000):
	ims2.append((plt.plot(resolve(tadd(add))[:,0],resolve(tadd(add))[:,1],'og',resolve(tadd(add))[:,2],resolve(tadd(add))[:,3],'ob')))

im_ani2 = animation.ArtistAnimation(fig2, ims2, interval = 50, repeat_delay = 300, blit = True)
im_ani2.save('trajet.mp4',writer=writer)