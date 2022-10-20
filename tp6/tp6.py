import random
from numpy import exp
import matplotlib.pyplot as plt
import time
import cv2


def main():
    
    path = input("Ingrese el directorio de la imagen: ")

    img = cv2.imread(path)
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rows, cols = grey.shape

    imgarray = [1] # entradas sin los bias

    for i in range(rows):
        for j in range(cols):
            imgarray.append(img[i, j][0])

    bias = 1
    sd = 0
    lr = 0.1

    no = int(input("Ingrese la cantidad de neuronas en la capa oculta: "))
    cantidad_pesos = ((len(imgarray) + 1) * no) + (no + 1)
    print(cantidad_pesos)

    pesos = [random.uniform(0.001,-0.001) for i in range(cantidad_pesos)]
    # pesos = []
    # for i in range(cantidad_pesos):
    #     pesos.append(random.uniform(0.001,-0.001))

    # print(f"Cantidad de pesos: {len(pesos)}")
    # input("ENTER...")

    iter = 0

    #entradas = [bias]
    # for element in imgarray:
    #     entradas.append(element)
    entradas = [n for n in imgarray]
    # entradas = list(map(lambda n: n, imgarray))
    print(f"Entradas = {len(entradas)}")
    input("ENTER...")

    inicio = time.time()

    while 1:

        iter += 1
        if iter == 11:
            final = time.time()
            print(f"Termino en {final - inicio} segundos")
            break

        print(f"Iteracion --> {iter}")

        # w = pesos.copy()

        salidas = []
        deltas_pesos_finales = []
        deltas_ocultas = []
        deltas = []


        aux = 0

        #for _ in range(no):
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
        print(f"Salida real = {y}")

        # calculo el error
        error = sd - y
        print(f"El error es {error}")
        # agrego el error a su lista correspondiente al igual que la salida
        #errores[cont].append(error)
        #salidas_reales[cont] = y

        delta_f = y * (1 - y) * error
        # con esto obtengo el delta_f

        deltas_pesos_finales = [lr * entrada * delta_f for entrada in entradas_temp]

        # for entrada in entradas_temp: # entradas = [1, salida1, salida2, salida3]
        #     delta_w = lr * entrada * delta_f
        #     deltas_pesos_finales.append(delta_w)
        # con esto obtengo [dw9, dw10, dw11, dw12]
        # print(f"Aca ldeltas finales son: {deltas_pesos_finales}")
        # print(f"Cantidad deltas pesos finales: {len(deltas_pesos_finales)}")
        # input("ENTER...")


        # print(f"Cantidad de salidas: {len(salidas)}")
        # input("ENTER...")

        deltas_ocultas = [salida * (1 - salida) * delta_f for salida in salidas]

        # for salida in salidas: # salidas = [salida1, salida2, salida3]
        #     deltas_ocultas.append(salida * (1 - salida) * delta_f)
        # con esto obtengo [delta_oc1, delta_oc2, delta_oc3]

        # print(f"Aca las deltas ocultas son: {deltas_ocultas}")
        # print(f"Cantidad deltas ocultas: {len(deltas_ocultas)}")
        # input("ENTER...")

        for delta_oculta in deltas_ocultas:
            deltas = [lr * entrada * delta_oculta for entrada in entradas]
            # deltas = list(map(lambda n: lr * n * delta_oculta, entradas))
            # for entrada in entradas:
            #     deltas.append(lr * entrada * delta_oculta)
        # con esto obtengo [dw0, dw1, dw2, dw3, dw4, dw5, dw6, dw7, dw8]
        # print(f"Aca las deltas son: {deltas}")
        # print(f"Cantidad deltas: {len(deltas)}")
        # input("ENTER...")

        deltas.extend(deltas_pesos_finales)
        # for element in deltas_pesos_finales:
        #     deltas.append(element)
        # con esto obtengo [dw0, dw1, dw2, dw3, dw4, dw5, dw6, dw7, dw8, dw9, dw10, dw11, dw12]
        # print(f"Cantidad deltas completa: {len(deltas)}")
        # input("ENTER...")

        # pesos = list(filter(lambda delta: pesos[deltas.index(delta)] + delta, deltas))
        # print(f"Cantidad de pesos: {len(pesos)}")
        # input("ENTER...")

        # a[:] = map(lambda x: -x, a)
        for i, delta in enumerate(deltas):
            pesos[i] = pesos[i] + delta
        # con esto obtengo los nuevos valores de los pesos

        # hago una copia de los nuevos pesos para poder manejarla
        #w = pesos.copy()
        # print(len(pesos))


if __name__ == '__main__':
    main()