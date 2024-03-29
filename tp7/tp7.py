import random
from numpy import exp
import numpy as np
import matplotlib.pyplot as plt
import time
import cv2



def calcular_salidas_imagenes_restantes(s, iter, pesos, aux_iters, imagen):

    aux_iters += [iter]

    labels = ['serious', 'surprised', 'worried']
    #no = int(input("Ingrese la cantidad de neuronas en la capa oculta: "))
    no = 10

    for label in labels:

        # for imagen in range(2):

        path = f'images/persona{imagen}/{label}.jpg'
        # print(f"Using image from {path}")

        img = cv2.imread(path)
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        rows, cols = grey.shape

        imgarray = [1]

        for i in range(rows):
            for j in range(cols):
                imgarray.append(img[i, j][0])

        bias = 1

        entradas = [n for n in imgarray]

        salidas = [bias]

        aux = 0

        for _ in range(no):

            primeros_pesos = [pesos[i] for i in range(aux, aux + len(entradas))]
            aux += len(entradas)

            x = sum(np.multiply(entradas, primeros_pesos))

            y = 1/(1 + exp(-x))

            salidas.append(y)


        cantidad_ultimos_pesos = no + 1
        ultimos_pesos = pesos[-cantidad_ultimos_pesos:]

        x = sum(np.multiply(salidas, ultimos_pesos))
        y = 1/(1 + exp(-x))
        if label == 'serious':
            if imagen == 0:
                s[0].append(y)
            elif imagen == 1:
                s[3].append(y)
        if label == 'surprised':
            if imagen == 0:
                s[1].append(y)
            elif imagen == 1:
                s[4].append(y)
        if label == 'worried':
            if imagen == 0:
                s[2].append(y)
            elif imagen == 1:
                s[5].append(y)
    
    if imagen == 0:
        plt.plot(aux_iters, s[0])
        plt.plot(aux_iters, s[1])
        plt.plot(aux_iters, s[2])
    elif imagen == 1:
        plt.plot(aux_iters, s[3])
        plt.plot(aux_iters, s[4])
        plt.plot(aux_iters, s[5])
    plt.pause(0.01)

    if iter == 100:
        aux_iters.clear()
        for n in range(6):
            s[n].clear()


def main():

    s = [[], [], [], [], [], []]
    aux_iters = []

    labels = ['angry', 'happy', 'joy', 'sad', 'serious_closed']
    errores = []
    for _ in range(len(labels)):
        errores += [],[]

    aux_imagenes = 0
    
    lr = 0.5
    #no = int(input("Ingrese la cantidad de neuronas en la capa oculta: "))
    no = 10

    pesos = []

    for label in labels:

        for imagen in range(2):

            path = f'images/persona{imagen}/{label}.jpg'
            print(f"Using image from {path}")

            img = cv2.imread(path)
            grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            rows, cols = grey.shape

            imgarray = [1]

            for i in range(rows):
                for j in range(cols):
                    imgarray.append(img[i, j][0])

            bias = 1
            if imagen == 0:
                sd = 0
            elif imagen == 1:
                sd = 1

            cantidad_pesos = ((len(imgarray)) * no) + (no + 1)
            print(cantidad_pesos)

            pesos = [random.uniform(0.01,-0.01) for _ in range(cantidad_pesos)]

            iter = 0
            printcounter = 0

            entradas = [n for n in imgarray]

            inicio = time.time()
            times_printed = 0

            while 1:

                iter += 1
                printcounter += 1
                if printcounter == 100:
                    times_printed += 1
                    final = time.time()
                    time_spent = final - inicio
                    print(f"Reached {printcounter * times_printed} itertions ({time_spent} seconds every {printcounter} iterations)")
                    printcounter = 0
                    inicio = time.time()
                if iter == 101:
                    break

                salidas = [bias]
                deltas_pesos_finales = []
                deltas_ocultas = []
                deltas = []

                aux = 0

                for _ in range(no):

                    primeros_pesos = [pesos[i] for i in range(aux, aux + len(entradas))]
                    aux += len(entradas)

                    x = sum(np.multiply(entradas, primeros_pesos))
        
                    y = 1/(1 + exp(-x))

                    salidas.append(y)


                cantidad_ultimos_pesos = no + 1
                ultimos_pesos = pesos[-cantidad_ultimos_pesos:]

                x = sum(np.multiply(salidas, ultimos_pesos))
                y = 1/(1 + exp(-x))

                # calculo el error
                error = sd - y
                errores[aux_imagenes] += [error]
                
                if label == 'angry':
                    calcular_salidas_imagenes_restantes(s, iter, pesos, aux_iters, imagen)

                if printcounter == 99:
                    print(f"Salida real = {y}")
                    print(f"Error = {error}")

                delta_f = y * (1 - y) * error

                deltas_pesos_finales = [lr * entrada * delta_f for entrada in salidas]

                salidas.remove(salidas[0]) # remuevo el bias de la lista de salidas

                deltas_ocultas = [salida * (1 - salida) * delta_f for salida in salidas]

                for delta_oculta in deltas_ocultas:
                    deltas += list(np.multiply(entradas, delta_oculta * lr))

                deltas.extend(deltas_pesos_finales)

                pesos = np.sum([pesos, deltas], axis=0)

                final = time.time()
            
            aux_imagenes += 1

    lista_iteraciones = []
    lista_iteraciones.extend(range(0, 100))
    plt.clf()
    plt.xlabel("Iteraciones")
    plt.ylabel("Errores")
    plt.title("GRÁFICO DE ERRORES")
    plt.axhline(y=0, color='black', linestyle='-')
    for cont in range(10):
        plt.plot(lista_iteraciones, errores[cont])
    plt.show()

    # plt.figure(figsize=(15,5))
    # plt.subplot(1, 2, 1)
    # plt.xlabel("Iteraciones")
    # plt.ylabel("Errores")
    # plt.title("GRÁFICO DE ERRORES")
    # plt.axhline(y=0, color='black', linestyle='-')
    # for cont in range(4):
    #     plt.plot(lista_iteraciones, errores[cont])
    # plt.subplot(1, 2, 2)
    # plt.xlabel("Iteraciones")
    # plt.ylabel("Pesos")
    # plt.title("GRÁFICO DE PESOS")
    # plt.axhline(y=0, color='black', linestyle='-')
    # for i in range(6):
    #     plt.plot(lista_iteraciones, s[i])
    # plt.show()



if __name__ == '__main__':
    main()