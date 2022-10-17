import random
import math
import matplotlib.pyplot as plt
import time

# calculos en la capa oculta
def calculos_ocultas(no, entradas, w, salidas):
    for _ in range(no):
        x = calcular_x(entradas, w)
        y = calcular_y(x)
        salidas.append(y)

# funcion para calcular x
def calcular_x(entradas, w):
    x = 0
    for entrada in entradas:
        x += entrada*w[0]
        w.remove(w[0])
        # voy removiendo para no tener que ir recorriendo la lista cambiando el indice
    return x

# funcion para calcular y
def calcular_y(x):
    return(1/(1 + math.exp(-x)))

# funcion para calcular el error
def calcular_error(sd, y):
    return(sd - y)

# funcion para calcular las deltas_ocultas
def calcular_delta_f(salida, delta):
    return(salida * (1 - salida) * delta)

def menu(e1, e2, sd, bias, pesos, no):
    print("\nTP4 - PERCEPTRON MULTICAPA CON BACK PROPAGATION PARA LA LOGICA XOR")
    print("-----------------------------------------------------------------")
    print("Tabla logica: ")
    print("\t| e1 | e2 | s |")
    print("\t---------------")
    for n in range(4):
        print(f"\t| {e1[n]}  | {e2[n]}  | {sd[n]} |")
    print(f"\nbias = {bias}")
    print(f"\nnumero de neuronas en la capa oculta = {no}")
    print("\nPesos sinopticos: ")
    for i, peso in enumerate(pesos):
        print(f"\tw{i} = {peso}")

def main():

    e1 = [0, 0, 1, 1]
    e2 = [0, 1, 0, 1]
    sd = [0, 1, 1, 0]

    bias = 1

    #no = 3# 4 --> prueba con una neurona mas (funciona)

    no = int(input("Ingrese la cantidad de neuronas en la capa oculta: "))
    cantidad_pesos = math.trunc((no * 13)/3)

    # aca se van a ir almacenando los errores en 4 listas distintas
    errores = [[], [], [], []]

    #        w0   w1   w2   w3   w4   w5   w6    w7   w8    w9     w10   w11   w12
    #pesos = [0.9, 0.7, 0.5, 0.3, -0.9, -1, 0.8, 0.35, 0.1, -0.23, -0.79, 0.56, 0.6] #, -0.5, 0.2, -0.1, 0.15] #--> prueba con una neurona mas (funciona)
    pesos = []
    for i in range(cantidad_pesos):
        pesos.append(random.uniform(1,-1))

    # aca se va a ir almacenando una lista por cada peso sinoptico
    #              w0  w1  w2  w3  w4  w5  w6  w7  w8  w9 w10 w11 w12
    #lista_pesos = [[], [], [], [], [], [], [], [], [], [], [], [], []]# , [], [], [], []] #--> prueba con una neurona mas (funciona)
    lista_pesos = []
    for i in range(cantidad_pesos):
        lista_pesos.append([])


    menu(e1, e2, sd, bias, pesos, no)

    lr = float(input("\n¿Que tasa de aprendizaje (learning rate) desea? --> "))

    limite_iteraciones = int(input("\n¿Cuántas iteraciones desea realizar? --> "))

    inicio = time.time()

    iteraciones = 0

    # copio los elementos de la lista sd pero van a ir cambiando por las salidas reales apenas se realice su calculo
    salidas_reales = sd.copy()

    while True:

        iteraciones += 1

        # voy agregando los pesos a su lista correspondiente. ej: w0 se almacena en lista_pesos[0] 
        for i, peso in enumerate(pesos):
            lista_pesos[i].append(peso)

        for cont in range(4):

            # hago una copia de los pesos para poder manejarla sin modificar la original
            w = pesos.copy()

            # while True:
            entradas = [bias, e1[cont], e2[cont]]
            salidas = [] # esto va a almacenar las salidas de la capa oculta
            deltas_pesos_finales = [] # esto va a almacenar dw9, dw10, dw11 y dw12
            deltas = [] # esto va a almacenar desde dw0 hasta dw8 y posteriormente todas las dw
            deltas_ocultas = [] # esto va a almacenar delta_oc1, delta_oc2 y delta_oc3

            calculos_ocultas(no, entradas, w, salidas)
            # con esto hago los calculos de las neuronas ocultas y guardo las salidas en una lista

            entradas = [bias]
            for element in salidas:
                entradas.append(element)
            # esto me deja entradas = [v, salida1, salida2, salida3]

            # aca hago los calculos de la neurona de salida
            x = calcular_x(entradas, w)
            y = calcular_y(x)

            # calculo el error
            error = calcular_error(sd[cont], y)
            # agrego el error a su lista correspondiente al igual que la salida
            errores[cont].append(error)
            salidas_reales[cont] = y

            delta_f = calcular_delta_f(y, error) 
            # con esto obtengo el delta_f

            for entrada in entradas: # entradas = [1, salida1, salida2, salida3]
                delta_w = lr * entrada * delta_f
                deltas_pesos_finales.append(delta_w)
            # con esto obtengo [dw9, dw10, dw11, dw12]

            for salida in salidas: # salidas = [salida1, salida2, salida3]
                deltas_ocultas.append(salida * (1 - salida) * delta_f)
            # con esto obtengo [delta_oc1, delta_oc2, delta_oc3]

            entradas = [bias, e1[cont], e2[cont]]
            for delta_oculta in deltas_ocultas:
                for entrada in entradas:
                    deltas.append(lr * entrada * delta_oculta)
            # con esto obtengo [dw0, dw1, dw2, dw3, dw4, dw5, dw6, dw7, dw8]

            for element in deltas_pesos_finales:
                deltas.append(element)
            # con esto obtengo [dw0, dw1, dw2, dw3, dw4, dw5, dw6, dw7, dw8, dw9, dw10, dw11, dw12]

            for i, delta in enumerate(deltas):
                pesos[i] = pesos[i] + delta
            # con esto obtengo los nuevos valores de los pesos

            # hago una copia de los nuevos pesos para poder manejarla
            w = pesos.copy()
            
        if iteraciones == limite_iteraciones:
            final = time.time()
            print(f"Elapsed time: {final-inicio} s")
            break
    
    print(f"\nResultados despues de {iteraciones} iteraciones:\n")
    print("\t| e1 | e2 | salida |  error ")
    print("\t------------------------------")
    for cont in range(4):
        print(f"\t| {e1[cont]}  | {e2[cont]}  | {round(salidas_reales[cont], 4)} | {round(errores[cont][-1], 4)} ")
    
    lista_iteraciones = []
    for i in range(limite_iteraciones):
        lista_iteraciones.append(i)

    while True:
        print("\nQue desea graficar?\n")
        print("\t1. Grafico de errores.")
        print("\t2. Grafico de pesos sinopticos.")
        print("\t3. Graficar ambos.")
        print("\t4. Salir.")
        selected = int(input("\tIngrese la opcion deseada: "))
        if selected == 1:
            plt.xlabel("Iteraciones")
            plt.ylabel("Errores")
            plt.title("GRÁFICO DE ERRORES")
            plt.axhline(y=0, color='black', linestyle='-')
            for cont in range(4):
                plt.plot(lista_iteraciones, errores[cont], label=f"error{cont}")
            plt.legend()
            plt.show()
        elif selected == 2:
            plt.xlabel("Iteraciones")
            plt.ylabel("Pesos")
            plt.title("GRÁFICO DE PESOS")
            plt.axhline(y=0, color='black', linestyle='-')
            for i, element in enumerate(lista_pesos):
                plt.plot(lista_iteraciones, element, label=f"w{i}")
            plt.legend()
            plt.show()
        elif selected == 3:
            plt.figure(figsize=(15,5))
            plt.subplot(1, 2, 1)
            plt.xlabel("Iteraciones")
            plt.ylabel("Errores")
            plt.title("GRÁFICO DE ERRORES")
            plt.axhline(y=0, color='black', linestyle='-')
            for cont in range(4):
                plt.plot(lista_iteraciones, errores[cont], label=f"error{cont}")
            plt.legend()
            plt.subplot(1, 2, 2)
            plt.xlabel("Iteraciones")
            plt.ylabel("Pesos")
            plt.title("GRÁFICO DE PESOS")
            plt.axhline(y=0, color='black', linestyle='-')
            for i, element in enumerate(lista_pesos):
                plt.plot(lista_iteraciones, element, label=f"w{i}")
            plt.legend()
            plt.show()
        elif selected == 4:
            break
        else:
            print("Ingrese una opcion valida.")


if __name__ == '__main__':
    main()