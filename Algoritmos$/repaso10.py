def recorrer(diccionario):
    for x in diccionario:
        print(f"ID {x} para el PRODUCTO {diccionario[x]}")
        print(f"El PRODUCTO {diccionario[x]}, tiene la ID {x}")
        print("<-<-<-<-<-<-<-<-<-<-<")

def insertar(nuevo):
    diccionario.update(nuevo)

def modificar(diccionario, clave, nuevoValor):
    for x in diccionario:
        if x==clave:
            diccionario[x]=nuevoValor

diccionario = {
    1: ["Galletas", 1.25, True],
    2: ["Chocolates", 5.50, True], # Nótese que se agreaga una coma en el final de esta línea
    3: ["Caramelos", 0.59, False]
}

recorrer(diccionario)
nuevoDiccionario = {4: ["Doritos", 0.75, True]}
print("")
insertar(nuevoDiccionario)
recorrer(diccionario)
print("")
nuevoPrecio = {}
# modificar(diccionario, 1.00, 4)
recorrer(diccionario)