#! /usr/bin/env python
# -*- coding: utf-8 -*-


#Semana 6 - Desafío 1
#Autores:    +Diego Caraballo +Ibán Sánchez Villanueva +Kelvin Provincia  
#Fecha:      29/05/13


#Especificaciones,
#Desarrollar un programa que permita crear diseños a partir de patrones y desplazamientos:
    #Los patrones pueden ser cualquier cadena de caracteres de una misma longitud y son ingresados por teclado.
    #Los patrones forman capas que se superponen. Las de nivel superior se hubican encima de las de un nivel inferior.
    #Para cada capa o patrón se define un desplazamiento que puede ser nulo, 1 o -1.
    
def creaDisenio():
	'''Permite crear diseños a partir de patrones
	y desplazamientos'''
	capas = int(input("¿Cuantas capas tendra el diseño?: "))
	ancho = int(input("¿Cual sera el ancho del patron?: "))
	serie = ""
	for i in range(ancho):
		serie += str((i+1)%10)
	disenio = []
	despla = []
	posicion = []
	for i in range( capas ):
		print("Introdusca el diseño de la capa", i,":")
		print(serie)
		print("|", " " * (ancho - 4), "|")
		dise = input("")
		if len(dise) < ancho:
			#llenar con espacios, si falto llenar el diseño hasta el ancho indicado
			dise += " " * ( ancho -  len(dise) )
		disenio.append(dise)
		despla.append(input("¿Cual sera el desplazamiento de esta capa (-1, 0, 1)?: "))
		print("")
		posicion.append(0)
	hiladas = int(input("¿Cuantas hiladas tendra el diseño?: "))
	
	for i in range(hiladas):
		linea = ((" ," * (ancho - 1)) + " ").split(",")
		for l in range(capas):		
			for c in range(ancho):
				if disenio[l][c] != " ":
					linea[c+posicion[l]-ancho] = disenio[l][c]
			posicion[l] += int(despla[l])
			if posicion[l] == ancho:
				posicion[l] = 0;
			if posicion[l] == -1:
				posicion[l] = ancho -1;
		print("".join(linea))
	
					
creaDisenio()
