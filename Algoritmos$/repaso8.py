# Función para RECORRER Y MOSTRAR LA LISTA
def recorrerRuta(lista):
    i = 0
    while i is not None: #Nótese que son de 2 variables
        valor, siguiente=lista[i]
        print(valor, end = " ---> ")
        break
    print("None")

# Ahora para BUSCAR CIUDADES, incluye mensaje si no se encuentra la ciudad
def buscarCiudad(ruta, ciudad):
    i = 0
    salida = f"El destino {ciudad} no existe"
    while i is not None:
        valor, siguiente=ruta[i]
        if valor==ciudad:
            salida=f"El destino {ciudad} existe"
            break
        i=siguiente
    print(salida)

def insertarCiudad(ruta, ciudad, nueva):
    i = 0
    while i is not None:
        valor, siguiente=ruta[i]
        if valor==ciudad:
            nuevo=len(ruta)
            ruta.append((nueva, siguiente))
            ruta[i]=(valor, nuevo)
            break
        i=siguiente

def eliminarCiudad(ruta, ciudad, borrar):
    i = 0
    while i is not None:
        valor, siguiente=ruta[i]
        if valor==ciudad:
            ruta.append((borrar, siguiente)) # Se agrega el valor y luego se agrega el puntero
            ruta[i+1]=(valor, borrar)
            break
        i=siguiente

rutaCiudades = [("Carchi", 1), ("Quito", 2), ("Cuenca", 3), ("Loja", None)]
recorrerRuta(rutaCiudades)
print("------------------------------------------------------------------------")

buscarCiudad(rutaCiudades, "Carchi")
print("------------------------------------------------------------------------")

insertarCiudad(rutaCiudades, "Quito", "Ambato")
print("------------------------------------------------------------------------")

eliminarCiudad(rutaCiudades, "Quito", "Loja")
print("------------------------------------------------------------------------")

 
