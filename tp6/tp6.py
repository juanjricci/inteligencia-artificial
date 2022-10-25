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

    for i in range(rows):
        for j in range(cols):
            imgarray.append(img[i, j][0])

    bias = 1
    sd = 0
    lr = 0.1

    #no = int(input("Ingrese la cantidad de neuronas en la capa oculta: "))
    no = 20
    cantidad_pesos = ((len(imgarray) + 1) * no) + (no + 1)
    print(cantidad_pesos)

    pesos = [random.uniform(0.001,-0.001) for _ in range(cantidad_pesos)]

    iter = 0
    printcounter = 0

    entradas = [n for n in imgarray]
    # print(f"Entradas = {len(entradas)}")
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
        if iter == 101:
            # final = time.time()
            # print(f"Termino en {final - inicio} segundos")
            break

        salidas = []
        deltas_pesos_finales = []
        deltas_ocultas = []
        deltas = []

        aux = 0
        n = 0

        while 1:

            if n == no:
                break

            x = 0

            for element in entradas:
                x += element * pesos[aux]
                aux += 1
                # w.remove(w[0])
 
            y = 1/(1 + exp(-x))

            salidas.append(y)
            # print(f"Cantidad de pesos restantes: {len(w)}")
            n += 1

        entradas_temp = [bias]
        for s in salidas:
            entradas_temp.append(s)

        for element in entradas_temp:
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

        deltas_pesos_finales = [lr * entrada * delta_f for entrada in entradas_temp]

        deltas_ocultas = [salida * (1 - salida) * delta_f for salida in salidas]

        deltas = [lr * entrada * delta_oculta for entrada, delta_oculta in zip(entradas, deltas_ocultas)]

        # for delta_oculta in deltas_ocultas:
        #     deltas = [lr * entrada * delta_oculta for entrada in entradas]

        deltas.extend(deltas_pesos_finales)

        for i, delta in enumerate(deltas):
            pesos[i] = pesos[i] + delta



if __name__ == '__main__':
    main()