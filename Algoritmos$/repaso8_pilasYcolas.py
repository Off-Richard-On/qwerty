# colas
from collections import deque

def recorrerCola(cola):
    for x in reversed(cola):
        print(f"[ { x } ]")

def eliminarBasic(): # Eliminiar BÁSICO o PRIMITIVO
    cola.remove(cola[0])

def eliminarConBiblioteca(cola):
    cola.popleft()

def insertar(nuevo):
    cola.append(nuevo)

cola=deque([5,2,6,3,9])
recorrerCola(cola)
print("-------------------------------------")

# Eliminando (se borra el ÚLTIMO ELEMENTO)
eliminarBasic()
recorrerCola(cola)
print("-------------------------------------")
eliminarConBiblioteca(cola)
recorrerCola(cola)

# Agregando (se incorpora al INICIO DE LA COLA)
print("-------------------------------------")
insertar("x")
recorrerCola(cola)