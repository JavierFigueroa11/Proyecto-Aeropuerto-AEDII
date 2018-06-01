"""rutasAleatorias crea un archivo con las rutas disponibles según la temporada que el usuario ingrese.
Se utiliza la librería csv para operar con este tipo de archivos y random para crear una aleatoridad de rutas."""

import csv
import random

__author__ = "Emiliano Calvacho"

def eleccion_temporada():
	"""
		Funcionamiento: el usuario ingresa una temporada
		Precondiciones: no recibe parametros
		Postcondiciones: devuelve la temporada elegida
	"""
	while True:
		print("Opciones de temporada:")
		print("1- Verano.\n2- Otoño.\n3- Invierno.\n4- Primavera.")
		temporada = int(input("Ingrese la temporada del año: "))
		if (temporada<1 or temporada>4):
			print("Por favor ingrese un temporada válido.")
		else:
			break
		
	return temporada

def list_ID_aeropuertos():
	"""
		Funcionamiento: se crea una lista con la identificación de los aeropuertos
		Precondiciones: no recibe parametros
		Postcondiciones: devuelve una lista de las ID de los aeropuertos
	"""
	with open('AeropuertosArg.csv') as archivo_csv:
		leer = csv.reader(archivo_csv)
		
		list_ID = []

		for linea in leer:
			list_ID.append(linea[0])

	return list_ID

def ruteoAleatorio():
	"""
		Funcionamiento: crea un archivo cvs con las rutas dispobibles aleatoriamente
		Precondiciones: no recibe parametros
		Postcondiciones: no devuelve nada
	"""
	temporada = eleccion_temporada()
	lista_ID = list_ID_aeropuertos()

	# Calculo la cantidad de aristas o rutas
	# Maximo de rutas: [v*(v-1)]/2, donde v son la cantidad de vertices, o sea la
	# longitud de lista_ID. Pero como maximo solo dejamos hasta 60 rutas.
	# Minimo de rutas: las que se desee. Pero vamos a poner hasta 25 rutas
	if temporada == 1:
		cant_aristas = random.randrange(25,61,1) # Del 25 a 61 de 1 en 1
	elif temporada == 2:
		cant_aristas = random.randrange(25,61,2) # Del 25 a 61 de 2 en 2
	elif temporada == 3:
		cant_aristas = random.randrange(25,61,3) # Del 25 a 61 de 3 en 3
	elif temporada == 4:
		cant_aristas = random.randrange(25,61,4) # Del 25 a 61 de 4 en 4

	# Se quitan 5 vértices para que queden aislados
	cont = 0
	while (cont < 5):
		a = random.choice(lista_ID)
		lista_ID.remove(a)
		cont += 1

	# print(lista_ID) # Imprimo la lista_ID sin los vértices aislados

	# Se buscan dos vértices aleatorios distintos y se los agrega en forma 
	# de tuplas a una lista de rutas. Esto se hace hasta que el contador
	# llegue a la cantidad de aristas que se desea.
	cont = 0
	lista_rutas = []
	while (cont <= cant_aristas):
		r1 = random.choice(lista_ID)
		r2 = random.choice(lista_ID)
		if (r1 != r2):
			t = (r1,r2)
			if (t not in lista_rutas):
				lista_rutas.append(t)
				cont += 1

	# c=1
	# for item in lista_rutas:
	# 	print(c,item)
	# 	c +=1

	# Creo el archivo de las rutas de los aeropuertos
	with open('RutasAeropuertos.csv', 'w',newline = '') as archivo_rutas:
		escribir = csv.writer(archivo_rutas)
		escribir.writerows(lista_rutas)

# Testing (para probar script quiten el comentario de la implementacion)
# ruteoAleatorio()

