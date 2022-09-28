import math
import matplotlib.pyplot as plt

# calculos en la capa oculta
def calculos_ocultas(no, entradas, w, salidas):
    for n in range(no):
        x = calcular_x(entradas, w)
        y = calcular_y(x)
        salidas.append(y)

# funcion para calcular x
def calcular_x(entradas, w):
    x = 0
    for entrada in entradas:
        x += entrada*w[0]
        w.remove(w[0]) # voy removiendo para no tener que ir recorriendo la lista cambiando el indice
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

def main():
    e1 = [0, 0, 1, 1]
    e2 = [0, 1, 0, 1]
    sd = [0, 1, 1, 0]

    v = 1

    lr = 0.5

    errores1 = []
    errores2 = []
    errores3 = []
    errores4 = []

    lista_pesos = [[], [], [], [], [], [], [], [], [], [], [], [], []]
    

    limite_iteraciones = 10000

    for cont in range(4):

        pesos = [0.9, 0.7, 0.5, 0.3, -0.9, -1, 0.8, 0.35, 0.1, -0.23, -0.79, 0.56, 0.6]
        
        # hago una copia de los pesos para poder manejarla sin modificar la original
        w = pesos.copy()

        no = 3
        iteraciones = 0

        while True:
            entradas = [v, e1[cont], e2[cont]]
            salidas = [] # esto va a almacenar las salidas de la capa oculta
            deltas_pesos_finales = [] # esto va a almacenar dw9, dw10, dw11 y dw12
            deltas = [] # esto va a almacenar desde dw0 hasta dw8 y posteriormente todas las dw
            deltas_ocultas = [] # esto va a almacenar delta_oc1, delta_oc2 y delta_oc3

            calculos_ocultas(no, entradas, w, salidas)
            # con esto hago los calculos de las neuronas ocultas y guardo las salidas en una lista

            entradas = [v]
            for element in salidas:
                entradas.append(element)
            # esto me deja entradas = [v, salida1, salida2, salida3]

            # aca hago los calculos de la neurona de salida
            x = calcular_x(entradas, w)
            y = calcular_y(x)

            # calculo el error
            error = calcular_error(sd[cont], y)
            if cont == 0:
                errores1.append(error)
            elif cont == 1:
                errores2.append(error)
            elif cont == 2:
                errores3.append(error)
            elif cont == 3:
                errores4.append(error)

            delta_f = calcular_delta_f(y, error) 
            # con esto obtengo el delta_f
            #print("delta_f = ", delta_f)

            for entrada in entradas: # entradas = [1, salida1, salida2, salida3]
                delta_w = lr * entrada * delta_f
                deltas_pesos_finales.append(delta_w)
            # con esto obtengo [dw9, dw10, dw11, dw12]
            #print("deltas_finales = ", deltas_pesos_finales)

            for salida in salidas: # salidas = [salida1, salida2, salida3]
                deltas_ocultas.append(salida * (1 - salida) * delta_f)
            # con esto obtengo [delta_oc1, delta_oc2, delta_oc3]
            #print("deltas_ocultas = ", deltas_ocultas)

            entradas = [v, e1[cont], e2[cont]]
            for delta_oculta in deltas_ocultas:
                for entrada in entradas:
                    deltas.append(lr * entrada * delta_oculta)
            # con esto obtengo [dw0, dw1, dw2, dw3, dw4, dw5, dw6, dw7, dw8]
            #print("deltas = ", deltas)

            for element in deltas_pesos_finales:
                deltas.append(element)
            # con esto obtengo [dw0, dw1, dw2, dw3, dw4, dw5, dw6, dw7, dw8, dw9, dw10, dw11, dw12]
            #print("todas_las_deltas = ", deltas)

            for i, delta in enumerate(deltas):
                if len(lista_pesos[i]) < limite_iteraciones:
                    lista_pesos[i].append(pesos[i])
                pesos[i] = pesos[i] + delta
            # con esto obtengo los nuevos valores de los pesos
            #print("pesos_cambiados = ", pesos)

            # hago una copia de los nuevo pesos para poder manejarla
            w = pesos.copy()

            iteraciones += 1
            if iteraciones == limite_iteraciones:
                break

        print(f"Salida real para la e1 = {e1[cont]}, e2 = {e2[cont]} y sd = {sd[cont]} despues de {iteraciones} iteraciones: {y}")
        print(f"El error es: {error}")
        print("---------------------------------------------------------------------------------")
    
    print(len(lista_pesos[0]))
    
    lista_iteraciones = []
    for i in range(limite_iteraciones):
        lista_iteraciones.append(i)

    while True:
        # print(f"Error1: {error0}")
        # print(f"Error2: {error1}")
        # print(f"Error3: {error2}")
        # print(f"Error4: {error3}")
        print("Que desea graficar?\n")
        print("\t1. Grafico de errores.")
        print("\t2. Grafico de pesos sinopticos.")
        print("\t3. Graficar ambos.")
        print("\t4. Salir.")
        selected = int(input("Ingrese la opcion deseada: "))
        if selected == 1:
            plt.xlabel("Iteraciones")
            plt.ylabel("Errores")
            plt.title("GRÁFICO DE ERRORES")
            plt.axhline(y=0, color='black', linestyle='-')
            plt.plot(lista_iteraciones, errores1)
            plt.plot(lista_iteraciones, errores2)
            plt.plot(lista_iteraciones, errores3)
            plt.plot(lista_iteraciones, errores4)
            plt.show()
        elif selected == 2:
            plt.xlabel("Iteraciones")
            plt.ylabel("Pesos")
            plt.title("GRÁFICO DE PESOS")
            plt.axhline(y=0, color='black', linestyle='-')
            for element in lista_pesos:
                plt.plot(lista_iteraciones, element)
            plt.show()
        elif selected == 3:
            plt.figure(figsize=(15,5))
            plt.subplot(1, 2, 1)
            plt.xlabel("Iteraciones")
            plt.ylabel("Errores")
            plt.title("GRÁFICO DE ERRORES")
            plt.axhline(y=0, color='black', linestyle='-')
            plt.plot(lista_iteraciones, errores1)
            plt.plot(lista_iteraciones, errores2)
            plt.plot(lista_iteraciones, errores3)
            plt.plot(lista_iteraciones, errores4)
            plt.subplot(1, 2, 2)
            plt.xlabel("Iteraciones")
            plt.ylabel("Pesos")
            plt.title("GRÁFICO DE PESOS")
            plt.axhline(y=0, color='black', linestyle='-')
            for element in lista_pesos:
                plt.plot(lista_iteraciones, element)
            plt.show()
        elif selected == 4:
            break
        else:
            print("Ingrese una opcion valida.")


if __name__ == '__main__':
    main()