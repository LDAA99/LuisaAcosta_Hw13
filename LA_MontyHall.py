import numpy as np
import matplotlib.pyplot as plt
import random


#Hay que desordenar la lista
def sort_doors():
	lista=['goat', 'goat', 'car']
	random.shuffle(lista)
	return lista


#elegir puerta
def choose_door():
	opciones=[0, 1, 2]
	a=np.random.choice(opciones)
	return a
	

#mostrar una puerta
def reveal_door(lista, choice):
	for i in range(len(lista)):
		if(i!=choice and lista[i]=='goat'):
			lista[i]='GOAT_MONTY'
			break #para que solo me modifique la 1 puerta que encuentre con una cabra
	return lista


#punto 5

def finish_game(lista, choice, change):
	if(change=="false"):
		return lista[choice]
	else:
		for i in range(len(lista)):
			if(i!=choice and lista[i]!='GOAT_MONTY'):
				return lista[i]

#ahora acoplar las funciones
lista=sort_doors()
choice=choose_door()
mostrar=reveal_door(lista, choice)
falsos=[]
verdaderos=[]

#100 veces con false
for i in range(100):
	a=finish_game(mostrar, choice, change="false")
	falsos.append(a)

#100 veces con true
for i in range(100):
	b=finish_game(mostrar, choice, change="true")
	verdaderos.append(b)


#probabilidad si no se cambia
a=falsos.count('car')
proba1=a/100.0

#probabilidad si se cambia
b=verdaderos.count('car')
proba2=b/100.0


print "La probabilidad de ganar el carro cuando no se cambia de puerta es", proba1, "en cambio, cuando se cambia es de", proba2




	













