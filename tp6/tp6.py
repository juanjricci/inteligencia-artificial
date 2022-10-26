from email.mime import image
import random
from numpy import exp
import numpy as np
import matplotlib.pyplot as plt
import time
import cv2


def main():

    labels = ['angry', 'happy', 'joy', 'sad', 'serious_closed']
    errores = []
    for _ in range(len(labels)):
        errores += [],[]

    aux_imagenes = 0
    
    lr = 0.5
    #no = int(input("Ingrese la cantidad de neuronas en la capa oculta: "))
    no = 100

    for label in labels:

        for imagen in range(2):

                  
            #path = input("Ingrese el directorio de la imagen: ")
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

            cantidad_pesos = ((len(imgarray) + 1) * no) + (no + 1)
            print(cantidad_pesos)

            pesos = [random.uniform(0.0001,-0.0001) for _ in range(cantidad_pesos)]

            iter = 0
            printcounter = 0

            entradas = [n for n in imgarray]
            primeros_pesos = [pesos[i] for i in range(len(entradas))]
            # for i in range(len(entradas)):
            #     primeros_pesos.append(pesos[i])
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
                if iter == 1001:
                    # final = time.time()
                    # print(f"Termino en {final - inicio} segundos")
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

                    # x = 0
                    # inicio = time.time()
                    x = sum(np.multiply(entradas, primeros_pesos))
                    # print(otro)
                    # print(len(otro))
                    # input("Enter...")
                    # x = sum(otro)
                    #x = sum(entradas[k]*pesos[k] for k in entradas)
                    # for element in entradas:
                    #     x += element * pesos[aux]
                    #     aux += 1
                        # w.remove(w[0])
                    # final = time.time()
                    # print(f"Calcular x tardo {final - inicio} segundos")
        
                    y = 1/(1 + exp(-x))
                    # print(f"Salida = {y}")

                    salidas.append(y)
                    # print(f"Cantidad de pesos restantes: {len(w)}")
                    n += 1

                # entradas_temp = [bias]
                # for s in salidas:
                #     entradas_temp.append(s)
                # inicio = time.time()
                for element in salidas: # aca la lista salidas contiene el bias mas las salidas de la capa oculta
                    x += element * pesos[aux]
                    # w.remove(w[0])
                # final = time.time()
                # print(f"Calcular x (salida) tardo {final - inicio} segundos")

                y = 1/(1 + exp(-x))
                # print(f"Salida real = {y}")

                # calculo el error
                error = sd - y
                errores[aux_imagenes] += [error]

                if printcounter == 99:
                    print(f"Salida real = {y}")
                    print(f"Error = {error}")
                # print(f"El error es {error}")
                # agrego el error a su lista correspondiente al igual que la salida
                #errores[cont].append(error)
                #salidas_reales[cont] = y

                delta_f = y * (1 - y) * error
                # con esto obtengo el delta_f
                # inicio = time.time()
                deltas_pesos_finales = [lr * entrada * delta_f for entrada in salidas]
                # final = time.time()
                # print(f"Calcular deltas pesos finales tardo {final - inicio} segundos")
                salidas.remove(salidas[0]) # remuevo el bias de la lista de salidas
                # inicio = time.time()
                deltas_ocultas = [salida * (1 - salida) * delta_f for salida in salidas]
                # final = time.time()
                # print(f"Calcular deltas ocultas tardo {final - inicio} segundos")
                # print(f"Deltas ocultas: {len(deltas_ocultas)}")
                # input("ENTER...")

                # inicio = time.time()
                deltas = [lr * entrada * delta_oculta for entrada, delta_oculta in zip(entradas, deltas_ocultas)]
                # final = time.time()
                # print(f"Calcular deltas tardo {final - inicio} segundos")

                # for delta_oculta in deltas_ocultas:
                #     deltas = [lr * entrada * delta_oculta for entrada in entradas]
                # inicio = time.time()
                deltas.extend(deltas_pesos_finales)
                # final = time.time()
                # print(f"Completar deltas tardo {final - inicio} segundos")

                # inicio = time.time()
                for i, delta in enumerate(deltas):
                    pesos[i] = pesos[i] + delta
                final = time.time()
                # print(f"Actualizar los pesos tardo {final - inicio} segundos")
            
            aux_imagenes += 1

    lista_iteraciones = []
    lista_iteraciones.extend(range(0, 1000))
    plt.xlabel("Iteraciones")
    plt.ylabel("Errores")
    plt.title("GRÁFICO DE ERRORES")
    plt.axhline(y=0, color='black', linestyle='-')
    for cont in range(10):
        plt.plot(lista_iteraciones, errores[cont])
    plt.show()



if __name__ == '__main__':
    main()