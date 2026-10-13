def recorrer(diccionario):
    for x in diccionario:
        print(f"Clave {x}, con valor {diccionario[x]}")

def insertar(nuevo):
    diccionario.update(nuevo)

def eliminar(clave):
    diccionario.pop(clave)

def buscar(diccionario, claveElemento):
    for x in diccionario:
        if x==claveElemento:
            salida=(f"El elemento {x} con valor {diccionario[x]} EXISTE")
            break
    print(salida)
    


diccionario = { # Los diccionarios UTILIZAN LLAVES {}
    1: "Ecuador",
    2: "Argentina", # NÓTESE QUE se agregan una coma al finalizar la línea
    3: "Suecia"
    }

# Se recorre el diccionario con BUCLE FOR
for x in diccionario:
    print(x, end=".- ") # Imprime solo claves
    print(f"Clave {x} con valor de {diccionario[x]}")

# Otra forma (my)
print("---------------------------------------------")
for x in diccionario:
    print(x, end=".- ") # Imprime solo claves
    print(f"Con valor de {diccionario[x]}")
print("---------------------------------------------")

# FUNCIONES:
print("CON FUNCIONES:")
recorrer(diccionario)

pais={4: "España"} # Se crea el diccionario

insertar(pais) # Se inserta los elementos del diccionario ya creado ("pais")
print("")
recorrer(diccionario) # Se muestra en pantalla los elementos con el nuevo país
print("")
eliminar(2) # Se elimina la CLAVE 2, que sería Argentina
recorrer(diccionario)
print("")
buscar(diccionario, 1) # Se manda a buscar el elemento 1 (ECUADOR)