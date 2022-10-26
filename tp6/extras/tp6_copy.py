import random
from numpy import exp
import matplotlib.pyplot as plt
import time
import cv2


def main():
    
    #path = input("Ingrese el directorio de la imagen: ")
    path = 'images/persona0/angry.jpg'

    img = cv2.imread(path)
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rows, cols = grey.shape

    imgarray = [1]
    imgdict = {}

    for i in range(rows):
        for j in range(cols):
            imgarray.append(img[i, j][0])

    for i in range(len(imgarray)):
        imgdict[i] = imgarray[i]

    # print(imgdict)
    # input('ENTER...')

    bias = 1
    sd = 0
    lr = 0.1

    #no = int(input("Ingrese la cantidad de neuronas en la capa oculta: "))
    no = 10
    cantidad_pesos = ((len(imgarray) + 1) * no) + (no + 1)
    print(cantidad_pesos)

    # pesos = [random.uniform(0.001,-0.001) for _ in range(cantidad_pesos)]
    pesos = {}
    for i in range(cantidad_pesos):
        pesos[i] = random.uniform(0.001,-0.001)
    # pesos = {random.uniform(0.001,-0.001) for _ in range(cantidad_pesos)}
    # print(pesos)
    # input("ENTER...")

    iter = 0
    printcounter = 0
    
    entradas = {}
    for n, element in imgdict.items():
        entradas[n] = element
    # entradas = [n for n in imgarray]
    # print(entradas)
    # input("ENTER...")

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
        if iter == 2:
            # final = time.time()
            # print(f"Termino en {final - inicio} segundos")
            break

        #salidas = [bias]
        salidas = {0: bias}
        #deltas_pesos_finales = []
        deltas_pesos_finales = {}
        # deltas_ocultas = []
        deltas_ocultas = {}
        # deltas = []
        deltas = {}

        aux = 0
        n = 0
        # cont_salidas = 1

        while 1:

            if n == no:
                break

            x = 0
            inicio = time.time()
            otro = entradas*pesos
            print(otro)
            input("Enter...")
            x = sum(entradas[k]*pesos[k] for k in entradas)
            # for element in entradas.values():
            #     x += element * pesos[aux]
            #     aux += 1
            #     # w.remove(w[0])
            final = time.time()
            print(f"Calcular x tardo {final - inicio} segundos")
 
            y = 1/(1 + exp(-x))
            salidas[n + 1] = y
            # print(salidas)
            # input("ENTER...")

            #salidas.append(y)
            # print(f"Cantidad de pesos restantes: {len(w)}")
            n += 1

        # entradas_temp = [bias]
        # for s in salidas:
        #     entradas_temp.append(s)

        for element in salidas.values(): # aca la lista salidas contiene el bias mas las salidas de la capa oculta
            x += element * pesos[aux]
            # w.remove(w[0])

        y = 1/(1 + exp(-x))
        # print(f"Salida real = {y}")

        # calculo el error
        error = sd - y
        # print(f"El error es {error}")
        # agrego el error a su lista correspondiente al igual que la salida
        #errores[cont].append(error)
        #salidas_reales[cont] = y

        delta_f = y * (1 - y) * error
        # con esto obtengo el delta_f
        for i, element in salidas.items():
            deltas_pesos_finales[i] = lr * element * delta_f
        # deltas_pesos_finales = [lr * entrada * delta_f for entrada in salidas]
        # print(deltas_pesos_finales)
        # input("ENTER...")
        salidas.pop(0) # remuevo el bias de la lista de salidas
        # print(salidas)
        # input("ENTER...")
        for i, salida in salidas.items():
            deltas_ocultas[i-1] = salida * (1 - salida) * delta_f
        # deltas_ocultas = [salida * (1 - salida) * delta_f for salida in salidas]
        # print(deltas_ocultas)
        # input("ENTER...")

        #deltas = [lr * entrada * delta_oculta for entrada, delta_oculta in zip(entradas, deltas_ocultas)]

        for delta_oculta in deltas_ocultas.values():
            for i, entrada in entradas.items():
                deltas[i] = lr * entrada * delta_oculta

        # print(deltas)
        # input("ENTER...")

        # for delta_oculta in deltas_ocultas:
        #     deltas = [lr * entrada * delta_oculta for entrada in entradas]

        #deltas.update(deltas_pesos_finales)
        for i, element in deltas_pesos_finales.items():
            deltas[len(deltas)] = element
        # print(deltas)
        # input("ENTER...")

        for i, delta in deltas.items():
            pesos[i] = pesos[i] + delta



if __name__ == '__main__':
    main()