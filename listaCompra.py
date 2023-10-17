#Primero creamos una lista de compra vacía:

listaCompra = []

#Después definimos las funciones para añadir y quitar artículos:

def añadirArticulo():
	listaCompra.append(input("Escribe el artículo que deseas añadir a continuación:"))
	print("Artículo añadido a la lista")
	
def quitarArticulo():
	listaCompra.remove(input("Escribe el artículo que deseas quitar a continuación:"))
	print("Artículo quitado de la lista")

#Luego establecemos el valor para preguntar si se quieren añadir artículos a True y creamos el bucle while para preguntarlo hasta que se responda que no:

preguntarUsuarioA = True

while preguntarUsuarioA == True:
	
	preguntarAñadirArticulo = input("¿Deseas añadir un artículo a la lista?")

	if preguntarAñadirArticulo == "S" or preguntarAñadirArticulo == "s":
		añadirArticulo()
		print("La lista actualmente contiene lo siguiente: " + str(listaCompra))
	
	if preguntarAñadirArticulo == "N" or preguntarAñadirArticulo == "n":
		print("No se añadirán más artículos. La lista es la siguiente: " + str(listaCompra))
		preguntarUsuarioA = False
		
#Después establecemos el valor para preguntar si se quieren quitar artículos a True y creamos el bucle while para preguntarlo hasta que se responda que no:
		
preguntarUsuarioQ = True

while preguntarUsuarioQ == True:
	
	preguntarQuitarArticulo = input("¿Deseas eliminar algún artículo de la lista?")
	
	if preguntarQuitarArticulo == "S" or preguntarQuitarArticulo == "s":
		quitarArticulo()
		print("La lista actualmente contiene lo siguiente: " + str(listaCompra))
	
	if preguntarQuitarArticulo == "N" or preguntarQuitarArticulo == "n":
		print("No se quitarán más artículos. La lista es la siguiente: " + str(listaCompra))
		preguntarUsuarioQ = False
		
# Y por último... Gracias!!!

print("Gracias por usar el programa!!!")


	

	

