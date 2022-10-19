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

    entradas = [bias]
    for element in imgarray:
        entradas.append(element)

    print(len(entradas))

    no = int(input("Ingrese la cantidad de neuronas en la capa oculta: "))
    cantidad_pesos = ((len(imgarray) + 1) * no) + (no + 1)

    pesos = []
    for i in range(cantidad_pesos):
        pesos.append(random.uniform(0.001,-0.001))

    print(len(pesos))

    w = pesos.copy()

    salidas = []

    for _ in range(no):

        x = 0

        for element in entradas:
            x += element * w[0]
            w.remove(w[0])

        y = 1/(1 + math.exp(-x))

        salidas.append(y)
        print(f"Cantidad de pesos restantes: {len(w)}")

    entradas = [bias]
    for s in salidas:
        entradas.append(s)
        print(entradas)

    for element in entradas:
        x += element * w[0]
        w.remove(w[0])

    y = 1/(1 + math.exp(-x))
    print(f"Salida real = {y}")        


if __name__ == '__main__':
    main()