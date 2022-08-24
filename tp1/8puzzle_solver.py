from collections import deque
from random import shuffle

#Clase que define un nodo en el 8-puzzle.
class Nodo:
    def __init__(self, estado, padre, movimiento, profundidad, piezas_correctas):        
        self.estado = estado                        #Posición atual de las piezas.
        self.padre = padre                          #Nodo desde el que se llega a este nodo.
        self.movimiento = movimiento                #Movimiento para encontrar este nodo desde el padre.
        self.profundidad = profundidad              #Posición del nodo en el árbol de búsqueda.
        self.piezas_correctas = piezas_correctas    #Total de piezas en su lugar para este estado.

    def moveUp(self):
        estado = list(self.estado)
        ind = estado.index(0)
        if ind - 3 >= 0:
            aux = estado[ind - 3]
            estado[ind - 3] = estado[ind]
            estado[ind] = aux
            return tuple(estado)
        return None

    def moveRight(self):
        estado = list(self.estado)
        ind = estado.index(0)
        if ind % 3 < 2:
            aux = estado[ind + 1]
            estado[ind + 1] = estado[ind]
            estado[ind] = aux
            return tuple(estado)
        return None

    def moveLeft(self):
        estado = list(self.estado)
        ind = estado.index(0)
        if ind % 3 > 0:
            aux = estado[ind - 1]
            estado[ind - 1] = estado[ind]
            estado[ind] = aux
            return tuple(estado)
        return None

    def moveDown(self):
        estado = list(self.estado)
        ind = estado.index(0)
        if ind + 3 < len(estado):
            aux = estado[ind + 3]
            estado[ind + 3] = estado[ind]
            estado[ind] = aux
            return tuple(estado)
        return None   

    #Método que encuentra y regresa todos los nodos sucesores del nodo actual.
    def encontrar_sucesores(self):
        sucesores = []
        sucesorUp = self.moveUp()
        sucesorDown = self.moveDown()
        sucesorRight = self.moveRight()
        sucesorLeft = self.moveLeft()
        
        sucesores.append(Nodo(sucesorUp, self, "arriba", self.profundidad + 1, calcular_heuristica(sucesorUp)))
        sucesores.append(Nodo(sucesorDown, self, "abajo", self.profundidad + 1, calcular_heuristica(sucesorDown)))
        sucesores.append(Nodo(sucesorRight, self, "derecha", self.profundidad + 1, calcular_heuristica(sucesorRight)))
        sucesores.append(Nodo(sucesorLeft, self, "izquierda", self.profundidad + 1, calcular_heuristica(sucesorLeft)))
        
        sucesores = [nodo for nodo in sucesores if nodo.estado != None]  
        return sucesores

    #Método que encuentra el camino desde el nodo inicial hasta el actual.
    def encontrar_camino(self, inicial):
        camino = []
        nodo_actual = self
        while nodo_actual.profundidad >= 1:
            camino.append(nodo_actual)
            nodo_actual = nodo_actual.padre
        camino.reverse()
        return camino

    #Método que imprime ordenadamente el estado (piezas) de un nodo.
    def imprimir_nodo(self):
        renglon = 0
        for pieza in self.estado:
            if pieza == 0:
                print(" ", end = " ")
            else:
                print (pieza, end = " ")
            renglon += 1
            if renglon == 3:
                print()
                renglon = 0       

#Función que calcula la cantidad de piezas que están en su lugar para un estado dado.
def calcular_heuristica(estado):
    correcto = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    valor_correcto = 0
    piezas_correctas = 0
    if estado:
        for valor_pieza, valor_correcto in zip(estado, correcto):
            if valor_pieza == valor_correcto:
                piezas_correctas += 1
            valor_correcto += 1
    return piezas_correctas   

#Algoritmo Breadth First Search(anchura).
def anchura(inicial, meta):
    visitados = set()   #Conjunto de estados visitados para no visitar el mismo estado más de una vez.
    frontera = deque()  #Cola de nodos aún por explorar. Se agrega el nodo inicial.  
    frontera.append(Nodo(inicial, None, None, 0, calcular_heuristica(inicial)))
    
    while frontera:                         #Mientras haya nodos por explorar:
        nodo = frontera.popleft()           #Se toma el primer nodo de la cola.

        if nodo.estado not in visitados:    #Si no se había visitado, 
            visitados.add(nodo.estado)      #se agrega al conjunto de visitados.
        else:                               #Si ya se había visitado
            continue                        #se ignora.
        
        if nodo.estado == meta:                         #Si es una meta, 
            print("\n¡Se encontró la meta!")            
            return nodo.encontrar_camino(inicial)       #se regresa el camino para llegar a él y termina el algoritmo.        
        else:                                           #Si no es una meta, 
            frontera.extend(nodo.encontrar_sucesores()) #se agregan sus sucesores a los nodos por explorar.

def random():
    print("funcion random")

def bidireccional():
    print("bidireccional")

#Función main.
def main():
    for i in range (50):
        lista = list(range(9))
        shuffle(lista)
    
    lista1=tuple(lista)

    estado_final = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    estado_inicial = lista1
    #estado_inicial = (1, 2, 3, 4, 5, 0, 7, 8, 6)   #De este estado se puede resolver en un movimiento.

    #Menú principal
    print("Este programa encuentra la solución al 8-puzzle utilizando diferentes algoritmos.")
    print("El estado inicial del juego es: ")
    (Nodo(estado_inicial, None, None, 0, calcular_heuristica(estado_inicial))).imprimir_nodo()
    print("\nMETODOS DE RESOLUCIÓN: ")
    print("\t1. Metodo de exploracion de anchura.")
    print("\t2. Busqueda bidireccional.")
    print("\t3. Busqueda Random.")
    print("\t4. Salir.")
    algoritmo = int(input("Ingrese el número de la opción que desee: "))

    #Selección de algoritmo
    if algoritmo == 1:
        print("Corriendo Método de exploración de anchura. Por favor espere.")
        nodos_camino = anchura(estado_inicial, estado_final)
    elif algoritmo == 2:
        print("Corriendo RANDOM. Por favor espere.")
    elif algoritmo == 3:
        print("Corriendo BIDIRECCIONAL. Por favor espere.")
    else:
        return 0

    #Se imprime el camino si existe y si el usuario lo desea.
    if nodos_camino:
        print ("El camino tiene", len(nodos_camino), "movimientos.")
        imprimir_camino = (input ("¿Desea imprimir dicho camino? s/n: "))

        if imprimir_camino == "s" or imprimir_camino == "S":
            print("\nEstado inicial:")
            (Nodo(estado_inicial, None, None, 0, calcular_heuristica(estado_inicial))).imprimir_nodo()
            print ("Piezas correctas:", calcular_heuristica(estado_inicial), "\n")
            input("Presione \"enter\" para continuar.")
            
            for nodo in nodos_camino:
                print("\nSiguiente movimiento:", nodo.movimiento)
                print("Estado actual:")
                nodo.imprimir_nodo()
                print("Piezas correctas:", nodo.piezas_correctas, "\n")     
                input("Presione \"enter\" para continuar.")
    else:
        print ("\nNo se encontró un camino con las condiciones dadas.")

    return 0    

if __name__ == "__main__":
    main()