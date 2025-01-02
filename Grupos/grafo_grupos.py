import numpy as np 
L=np.array([[1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	    [-1,2,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	    [0,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	    [0,0,0,2,-1,0,-1,0,0,0,0,0,0,0,0,0,0,0,0],
	    [0,0,-1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	    [0,0,0,-1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
	    [-1,0,0,0,0,-1,2,0,0,0,0,0,0,0,0,0,0,0,0],
	    [0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0],
	    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	    [0,0,0,0,0,0,0,-1,-1,3,-1,0,0,0,0,0,0,0,0],
	    [0,0,0,0,0,0,0,-1,0,0,2,-1,0,0,0,0,0,0,0],
	    [0,0,0,0,0,0,0,-1,0,0,0,2,-1,0,0,0,0,0,0],
	    [0,0,0,0,0,0,0,-1,0,0,0,0,2,-1,0,0,0,0,0],
	    [0,0,0,0,0,0,0,-1,-1,0,0,0,0,2,0,0,0,0,0],
	    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0],
	    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,-1,-1,0],
	    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,-1],
	    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,1,0],
	    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1]])
N=19
#print(L) # matriz laplaciana asociada al sistema X'=-LX.
X_n=np.array([14,14.1,15.6,15.4,15.8,16.7,17,3,3.4,4,4.5,5,6,7,-3.1,-2.2,-2,-1,0])
media=0
for i in range(0,N):
	media= media + X_n[i]
media = media/N
#print(X_n[1])
h=0.0001 #paso de tiempo
t_inicial=0
tFinal=10
num_iter=int(tFinal/h)
datos = open('grafo_grupos.txt','w')
def f(X,L):
	return np.dot(-1*L,X)
def calculaK1(X_n):
	return f(X_n,L)
def calculaK2(X_n,h,K1):
	return f(X_n+(h/2)*K1,L)
def calculaK3(X_n,h,K2):
	return f(X_n+(h/2)*K2,L)
def calculaK4(X_n,h,K3):
	return f(X_n+h*K3,L)
def introducir(X_n,i):
	datos.write('{0:.6f}\t'.format(X_n[i]))
def calculaMedia(X_n,N):
	media = 0
	for i in range(1,N):
		media = media + X_n[i]
	media = media/N
	return media 
def introducir_tiempo(t):
	datos.write('{0:.6f}\t'.format(t))
def introduce_salto():
	datos.write('\n')
def introduce_media(media):
	datos.write('{0:.4f}\t'.format(media))
#introducimos el dato inicial en el archivo de texto
introducir_tiempo(t_inicial)
for i in range(0,N):
	introducir(X_n,i)
introduce_media(media)
introduce_salto()
#hacemos las iteraciones principales 
for i in range(1,num_iter+1):
	K1=calculaK1(X_n)
	K2=calculaK2(X_n,h,K1)
	K3=calculaK3(X_n,h,K2)
	K4=calculaK4(X_n,h,K3)
	X_n= X_n +(h/6)*(K1+2*K2+2*K3+K4)
	t=t_inicial+i*h
	introducir_tiempo(t)
	for j in range(0,N):
		introducir(X_n,j)
	media=calculaMedia(X_n,N)
	introduce_media(media)
	introduce_salto()
datos.close()