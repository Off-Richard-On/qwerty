def recorrerPila(pila):
    for x in reversed(pila):
        print(f"[ {x} ]")

def eliminar():
    pila.pop()

def insertar(nuevo):
    pila.append(nuevo)



pila = [5,2,6,3,9]
recorrerPila(pila)
print("-----------------------------")
eliminar()
print("-----------------------------")
insertar("x")

