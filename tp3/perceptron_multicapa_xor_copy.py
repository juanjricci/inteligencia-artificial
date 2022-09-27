from copy import copy
import math


# realizo los calculos para la capa de entrada
def calculos_entradas(ne, v, e1, e2, w0, w1, w2, w3, w4, w5):
    for i in range(ne):
        if i == 0:
            x = calcular_x(v, e1, e2, w0, w1, w2, 0, 0)
            y_n0 = calcular_y(x)
        if i == 1:
            x = calcular_x(v, e1, e2, w3, w4, w5, 0, 0)
            y_n1 = calcular_y(x)
    return y_n0, y_n1

def calculos_ocultas(no, entradas, w, salidas):
    for n in range(no):
        x = calcular_x(entradas, w)
        y = calcular_y(x)
        salidas.append(y)

def calcular_x(entradas, w):
    x = 0
    for entrada in entradas:
        x += entrada*w[0]
        w.remove(w[0])
    return x


# funcion para calcular y
def calcular_y(x):
    return(1/(1 + math.exp(-x)))

def calcular_error(sd, y):
    return(sd - y)

def calcular_deltas_ocultas(salida, delta):
    return(salida * (1 - salida) * delta)

def calcular_deltas_pesos(entradas, delta_f, w, pesos):
    for i, entrada in enumerate(entradas):
        pesos[len(w) - len(entradas) + i] = (0.1 + entrada + delta_f) + w[len(pesos) - len(entradas)]
        w.remove(w[len(pesos) - len(entradas)])

def main():
    # e1 = [0, 0, 1, 1]
    # e2 = [0, 1, 0, 1]
    # sd = [0, 1, 1, 0]

    e1 = 0
    e2 = 0
    sd = 0

    v = 1

    pesos = [0.9, 0.7, 0.5, 0.3, -0.9, -1, 0.8, 0.35, 0.1, -0.23, -0.79, 0.56, 0.6]
    print('pesos iniciales', pesos)
    w = pesos.copy()

    no = 3
    iteraciones = 0

    while True:
        entradas = [v, e1, e2]
        salidas = []
        deltas_pesos_finales = []
        deltas = []
        deltas_ocultas = []

        iteraciones += 1
        if iteraciones == 1001:
            break

        calculos_ocultas(no, entradas, w, salidas)

        entradas = [v]
        for element in salidas:
            entradas.append(element)

        x = calcular_x(entradas, w)
        y = calcular_y(x)

        error = calcular_error(sd, y)

        w = pesos.copy()

        delta_f = calcular_deltas_ocultas(y, error) 
        # con esto obtengo el delta_f
        print("delta_f = ", delta_f)

        for entrada in entradas: # entradas = [1, salida1, salida2, salida3]
            delta_w = 0.1 * entrada * delta_f
            deltas_pesos_finales.append(delta_w)
        # con esto obtengo [dw9, dw10, dw11, dw12]
        print("deltas_finales = ", deltas_pesos_finales)

        for salida in salidas: # salidas = [salida1, salida2, salida3]
            deltas_ocultas.append(salida * (1 - salida) * delta_f)
        # con esto obtengo [delta_oc1, delta_oc2, delta_oc3]
        print("deltas_ocultas = ", deltas_ocultas)

        entradas = [v, e1, e2]
        for delta_oculta in deltas_ocultas:
            for entrada in entradas:
                deltas.append(0.1 * entrada * delta_oculta)
        # con esto obtengo [dw0, dw1, dw2, dw3, dw4, dw5, dw6, dw7, dw8]
        print("deltas = ", deltas)

        for element in deltas_pesos_finales:
            deltas.append(element)
        # con esto obtengo [dw0, dw1, dw2, dw3, dw4, dw5, dw6, dw7, dw8, dw9, dw10, dw11, dw12]
        print("todas_las_deltas = ", deltas)

        for i, delta in enumerate(deltas):
            pesos[i] = pesos[i] + delta
        # con esto obtengo los nuevos valores de los pesos
        print("pesos_cambiados = ", pesos)

        print("Salida real", y)


if __name__ == '__main__':
    main()