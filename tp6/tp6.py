import random
import math
import matplotlib.pyplot as plt
import time
import cv2


def main():
    
    path = input("Ingrese el directorio de la imagen: ")

    img = cv2.imread(path)
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rows, cols = grey.shape

    imgarray = [] # entradas sin los bias

    for i in range(rows):
        for j in range(cols):
            imgarray.append(img[i, j][0])

    bias = 1
    sd = 0
    lr = 0.5

    no = int(input("Ingrese la cantidad de neuronas en la capa oculta: "))
    cantidad_pesos = ((len(imgarray) + 1) * no) + (no + 1)

    pesos = []
    for i in range(cantidad_pesos):
        pesos.append(random.uniform(0.001,-0.001))

    # print(f"Cantidad de pesos: {len(pesos)}")
    # input("ENTER...")

    iter = 0

    while True:

        iter += 1
        if iter == 1000:
            break

        print(f"Iteracion --> {iter}")

        w = pesos.copy()

        salidas = []
        deltas_pesos_finales = []
        deltas_ocultas = []
        deltas = []

        entradas = [bias]
        for element in imgarray:
            entradas.append(element)

        for _ in range(no):

            x = 0

            for element in entradas:
                x += element * w[0]
                w.remove(w[0])

            y = 1/(1 + math.exp(-x))

            salidas.append(y)
            # print(f"Cantidad de pesos restantes: {len(w)}")

        entradas_temp = [bias]
        for s in salidas:
            entradas_temp.append(s)

        for element in entradas_temp:
            x += element * w[0]
            w.remove(w[0])

        y = 1/(1 + math.exp(-x))
        print(f"Salida real = {y}")

        # calculo el error
        error = sd - y
        print(f"El error es {error}")
        # agrego el error a su lista correspondiente al igual que la salida
        #errores[cont].append(error)
        #salidas_reales[cont] = y

        delta_f = y * (1 - y) * error
        # con esto obtengo el delta_f

        for entrada in entradas_temp: # entradas = [1, salida1, salida2, salida3]
            delta_w = lr * entrada * delta_f
            deltas_pesos_finales.append(delta_w)
        # con esto obtengo [dw9, dw10, dw11, dw12]
        # print(f"Aca ldeltas finales son: {deltas_pesos_finales}")
        # print(f"Cantidad deltas pesos finales: {len(deltas_pesos_finales)}")
        # input("ENTER...")


        # print(f"Cantidad de salidas: {len(salidas)}")
        # input("ENTER...")

        for salida in salidas: # salidas = [salida1, salida2, salida3]
            deltas_ocultas.append(salida * (1 - salida) * delta_f)
        # con esto obtengo [delta_oc1, delta_oc2, delta_oc3]

        # print(f"Aca las deltas ocultas son: {deltas_ocultas}")
        # print(f"Cantidad deltas ocultas: {len(deltas_ocultas)}")
        # input("ENTER...")

        for delta_oculta in deltas_ocultas:
            for entrada in entradas:
                deltas.append(lr * entrada * delta_oculta)
        # con esto obtengo [dw0, dw1, dw2, dw3, dw4, dw5, dw6, dw7, dw8]
        # print(f"Aca las deltas son: {deltas}")
        # print(f"Cantidad deltas: {len(deltas)}")
        # input("ENTER...")

        for element in deltas_pesos_finales:
            deltas.append(element)
        # con esto obtengo [dw0, dw1, dw2, dw3, dw4, dw5, dw6, dw7, dw8, dw9, dw10, dw11, dw12]
        # print(f"Cantidad deltas completa: {len(deltas)}")
        # input("ENTER...")

        for i, delta in enumerate(deltas):
            pesos[i] = pesos[i] + delta
        # con esto obtengo los nuevos valores de los pesos

        # hago una copia de los nuevos pesos para poder manejarla
        #w = pesos.copy()
        # print(len(pesos))


if __name__ == '__main__':
    main()