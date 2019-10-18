import numpy as np
from scipy.integrate import odeint
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rc

rc('text', usetex=True)

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
urx0 = du*np.cos(radur)          #Posição x de Urano inicial
ury0 = du*np.sin(radur)	        #Posição y de Urano inicial
velur = omeur*du
velurx0 = velur*np.sin(radur)	#Velocidade x de Urano inicial
velury0 = -velur*np.cos(radur)	#Velocidade y de Urano inicial

#Posição de Netuno em 1960	

radnt = 288.38*np.pi/180  #Posição angular de Netuno em 1960
ntx0 = dn*np.cos(radnt)	    #Posição x de Netuno inicial
nty0 = dn*np.sin(radnt)      #Posição y de Netuno inicial
velnt = oment*dn
velntx0 = velnt*np.sin(radnt)	#Velocidade x de Netuno inicial
velnty0 = -velnt*np.cos(radnt)	#Velocidade y de Netuno inicial
	
x0 = [urx0, ury0, ntx0, nty0, velurx0, velury0, velntx0, velnty0]  #VALORES INICIAS


def model(x, t):
	urx, ury, ntx, nty, vel_urx, vel_ury, vel_ntx, vel_nty = x


	Rur = (urx**2 + ury**2)**1.5					#R DE URANO
	Rnt = (ntx**2 + nty**2)**1.5		            #R DE NETUNO
	Rur_nt = ((urx-ntx)**2 + (ury-nty)**2)**1.5		#R ENTRE NETUNO E URANO
	
	Gx = G/Rur_nt*(urx - ntx)
	Gy = G/Rur_nt*(ury - nty)
	Gur = G*M/Rur
	Gnt = G*M/Rnt
	

	v_ur_xpt = -Gur*urx - mn*Gx
	v_ur_ypt = -Gur*ury - mn*Gy
	v_nt_xpt = -Gnt*ntx + mu*Gx
	v_nt_ypt = -Gnt*nty + mu*Gy

	A = [vel_urx,vel_ury,vel_ntx,vel_nty,v_ur_xpt,v_ur_ypt,v_nt_xpt,v_nt_ypt]
	return A

t = np.arange(0,1000, 1)
x = odeint(model,x0,t)
#set(h,{'markers'},{12;5;9}) 

def resolve(t):
	return odeint(model, x0, t)

def tadd(add):
	return np.arange(1,add,1)

def resolveadd(t,e):
	return odeint(model,x0,np.arange(0,t,e))

Tur = odeint(model,x0,np.arange(0,26.8*np.pi,.1))
Tnt = odeint(model,x0,np.arange(0,52.5*np.pi,.1))

def fig0():
	fig0 = plt.figure(num=0, figsize = (12,8), dpi = 100)
	plt.plot(x[:,0], x[:,1], 'og', label = 'Urano')
	plt.plot(x[:,2], x[:,3], 'ob', label = 'Netuno')
	plt.xlabel('x')
	plt.ylabel('y')
	#plt.plot(x[:,4], x[:,5], 'g', label = 'Urano')  #urano
	#plt.plot(x[:,6], x[:,7], 'b', label = 'Netuno')  #netuno
	plt.legend()
	plt.show()

def ani1(t):
	ims = []
	fig1 = plt.figure(num=1, figsize = (12,12), dpi = 150)
	fig1.suptitle("Netuno e Urano")
	plt.plot([0],[0],'oy',ms=20)
	#fig1.legend()
	#U = resolve(t)
	for add in np.arange(t):
		plota = plt.plot(x[add,0],x[add,1],'oc', x[add,2],x[add,3],'ob',12, [0],[0],'oy', Tur[:,0], Tur[:,1], '--c', Tnt[:,2], Tnt[:,3], '--b',lw=1,ms=10)
		#fig1.legend()
		fig1.legend(iter(plota), ('Urano', 'Netuno'))
		ims.append((plota))
		#plt.legend()

	im_ani = animation.ArtistAnimation(fig1, ims, interval = 50, repeat_delay=300, blit=True)
	im_ani.save('gravit.mp4',writer=writer)
	fig1.clf()

def ani2(t,e):
	fig2 = plt.figure(num=2, figsize = (12,8), dpi = 100)
	fig2.suptitle("Trajetoria da Orbita", fontsize =12)
	ims2 = []
	for add in np.arange(1,t,1):
		U = resolveadd(add,e)
		plotar = plt.plot(U[:,0],U[:,1],'og',U[:,2],U[:,3],'oc')
		fig2.legend(iter(plotar), ('Urano', 'Netuno'))
		ims2.append((plotar))
	im_ani2 = animation.ArtistAnimation(fig2, ims2, interval = 50, repeat_delay = 300, blit = True)
	im_ani2.save('trajet.mp4',writer=writer)

def fototerra():
	fig3 = plt.figure()
	x = 3*np.cos(np.arange(0,2*np.pi+1,.1))
	y = 3*np.sin(np.arange(0,2*np.pi+1,.1))

	plt.plot(x,y,'--', lw=.5)
	plt.plot(3*np.cos(np.pi / 4), 3*np.sin(np.pi/4),'og',ms=5)
	plt.plot([0],[0],'oy',ms=10,label='')
	plt.axis([-4,4,-4,4])
	plt.show()

def onlyuranus(x, t):
	urx, ury, vel_urx, vel_ury = x


	Rur = (urx**2 + ury**2)**1.5					#R DE URANO
	Gur = G*M/Rur
	v_ur_xpt = -Gur*urx
	v_ur_ypt = -Gur*ury

	return [vel_urx, vel_ury, v_ur_xpt, v_ur_ypt]

def onlyneptune(x,t):
	ntx, nty, vel_ntx, vel_nty = x

	Rnt = (ntx**2 + nty**2)**1.5			#R DE NETUNO
	Gnt = G*M/Rnt

	v_nt_xpt = -Gnt*ntx
	v_nt_ypt = -Gnt*nty

	return [vel_ntx,vel_nty,v_nt_xpt,v_nt_ypt]

def onlyneptuneevol(t,n0):
	#movimento e velocidade netuno x sol
	SN = odeint(onlyneptune,n0,t)
	return SN

def onlyuranusevol(t,u0):
	#movimento e velocidade urano x sol
	SU = odeint(onlyuranus, u0,t)
	#SU1 = odeint(onlyuranus,u01,t)
	#plt.plot(t,SU[:,0])
	#plt.plot(t,SU1[:,0])
	#plt.show()
	return SU


def compare(tau):
	u0 = [urx0, ury0, velurx0, velury0]
	n0 = [ntx0, nty0,velntx0,velnty0]



	t = np.arange(0,tau,.1)
	TB = odeint(model,x0,t)
	U = onlyuranusevol(t,u0)
	N = onlyneptuneevol(t,n0)


	ru2 = (U[:,0]**2+U[:,1]**2)**.5
	ru3	= (TB[:,0]**2+TB[:,1]**2)**.5
	vu2 = (U[:,2]**2+U[:,3]**2)**.5
	vu3 = (TB[:,4]**2+TB[:,5]**2)**.5

	wu3 = vu3 / ru3 
	wu2 = vu2 / ru2
 
	rn2 = (N[:,0]**2+N[:,1]**2)**.5
	rn3	= (TB[:,2]**2+TB[:,3]**2)**.5
	vn2 = (N[:,2]**2+N[:,3]**2)**.5
	vn3 = (TB[:,6]**2+TB[:,7]**2)**.5

	wn3 = vn3 / rn2
	wn2 = vn2 / rn2

	plt.title('Velocidade Angular de Urano')
	plt.plot(t, wu2,label='$\omega_u$ sem perturbacao')
	plt.plot(t,wu3,label='$\omega_u$ com perturbacao')
	plt.xlabel('$t$')
	plt.ylabel('$\omega$')
	plt.legend()
	plt.show()

	plt.title('Velocidade Linear de Urano')
	plt.plot(t, vu2,label='$v_u$ sem perturbacao')
	plt.plot(t, vu3,label='$v_u$ com perturbacao')
	plt.xlabel('$t$')
	plt.ylabel('$v$')
	plt.legend()
	plt.show()

	plt.title('Distancia de Urano')
	plt.plot(t, ru2,label='$r_u$ sem perturbacao')
	plt.plot(t, ru3,label='$r_u$ com perturbacao')
	plt.xlabel('$t$')
	plt.ylabel('$r$')
	plt.legend()
	plt.show()

	plt.title('Velocidade Angular de Netuno')
	plt.plot(t, wn2,label='$\omega_n$ sem perturbacao')
	plt.plot(t, wn3,label='$\omega_n$ com perturbacao')
	plt.xlabel('$t$')
	plt.ylabel('$v$')
	plt.legend()
	plt.show()

#	plt.title('Velocidade Linear de Netuno')
#	plt.plot(t, vn2,label='$v_n$ sem perturbacao')
#	plt.plot(t, vn3,label='$v_n$ com perturbacao')
#	plt.xlabel('$t$')
#	plt.ylabel('$v$')
#	plt.legend()
#	plt.show()
	#plt.subplot(224)
#	plt.title('Distancia de Netuno')
#	plt.plot(t,rn2,'r',label='$r_n$ sem perturbacao')
#	plt.plot(t,rn3,'b',label='$r_n$ com perturbacao')
#	plt.xlabel('$t$')
#	plt.ylabel('$r$')
#	plt.legend()
	#plt.plot(t,vn2, t,vn3,'c',label='$v_n$ sem perturbacao')
	#plt.plot(t,wn3,'g',label='$v_n$ com perturbacao')
	#plt.plot(t,wn2,'r',label='$r_n$ sem perturbacao')
	#plt.plot(t,wn3,'r',label='$r_n$ sem perturbacao')

	plt.plot(t, rn3,t, rn2,label='$\omega_u$ sem perturbacao')
#	plt.plot(t,ru2,label='$\omega_u$ com perturbacao')

	plt.show()