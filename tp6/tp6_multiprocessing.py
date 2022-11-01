from multiprocessing import Process
import random
from numpy import exp
import numpy as np
import matplotlib.pyplot as plt
import time
import cv2



def main(proc, labels, errores, lr, no):

    for label in labels:

        path = f'images/persona{proc}/{label}.jpg'
        print(f"Using image from {path}")

        img = cv2.imread(path)
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        rows, cols = grey.shape

        imgarray = [1]

        for i in range(rows):
            for j in range(cols):
                imgarray.append(img[i, j][0])

        bias = 1
        if proc == 0:
            sd = 0
        elif proc == 1:
            sd = 1

        cantidad_pesos = ((len(imgarray) + 1) * no) + (no + 1)
        print(cantidad_pesos)

        pesos = [random.uniform(0.0001,-0.0001) for _ in range(cantidad_pesos)]

        iter = 0
        printcounter = 0

        entradas = [n for n in imgarray]
        primeros_pesos = [pesos[i] for i in range(len(entradas))]

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
            n = 0
        
            while 1:

                if n == no:
                    break

                x = sum(np.multiply(entradas, primeros_pesos))
    
                y = 1/(1 + exp(-x))

                salidas.append(y)

                n += 1

            for element in salidas: # aca la lista salidas contiene el bias mas las salidas de la capa oculta
                x += element * pesos[aux]

            y = 1/(1 + exp(-x))

            # calculo el error
            error = sd - y
            indice = labels.index(label)

            errores[indice] += [error]
            # print(errores)
            

            if printcounter == 99:
                print(f"Salida real = {y}")
                print(f"Error = {error}")

            delta_f = y * (1 - y) * error

            deltas_pesos_finales = [lr * entrada * delta_f for entrada in salidas]

            salidas.remove(salidas[0]) # remuevo el bias de la lista de salidas

            deltas_ocultas = [salida * (1 - salida) * delta_f for salida in salidas]

            # inicio = time.time()
            deltas = [lr * entrada * delta_oculta for entrada, delta_oculta in zip(entradas, deltas_ocultas)]

            deltas.extend(deltas_pesos_finales)

            for i, delta in enumerate(deltas):
                pesos[i] = pesos[i] + delta
            final = time.time()
            
        # aux_imagenes += 1
        errores_comp.append(errores[indice])
        print(errores_comp)



if __name__ == '__main__':
    errores_comp = []
    procs = []
    labels = ['angry', 'happy', 'joy', 'sad', 'serious_closed']
    errores = []
    for _ in range(len(labels)):
        errores.append([])

    print(errores)
    input("Enter...")

    # aux_imagenes = 0
    
    lr = 0.5
    #no = int(input("Ingrese la cantidad de neuronas en la capa oculta: "))
    no = 10

    for i in range(2):
        p = Process(target=main, args=(i, labels, errores, lr, no))
        p.start()
        procs.append(p)


    for proc in procs:
        proc.join()

    print(len(errores_comp))
    input("enter...")

    lista_iteraciones = []
    lista_iteraciones.extend(range(0, 1000))
    plt.xlabel("Iteraciones")
    plt.ylabel("Errores")
    plt.title("GRÁFICO DE ERRORES")
    plt.axhline(y=0, color='black', linestyle='-')
    for cont in range(10):
        plt.plot(lista_iteraciones, errores_comp[cont])
    plt.show()