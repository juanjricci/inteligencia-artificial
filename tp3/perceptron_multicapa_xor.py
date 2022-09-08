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

# realizo los calculos para la capa oculta
def calculos_ocultas(no, v, y_n0, y_n1, w6, w7, w8, w9, w10, w11, w12, w13, w14):
    for n in range(no):
        if n == 0:
            x = calcular_x(v, y_n0, y_n1, w6, w7, w8, 0, 0)
            y_n2 = calcular_y(x)
        if n == 1:
            x = calcular_x(v, y_n0, y_n1, w9, w10, w11, 0, 0)
            y_n3 = calcular_y(x)
        if n == 2:
            x = calcular_x(v, y_n0, y_n1, w12, w13, w14, 0, 0)
            y_n4 = calcular_y(x)
    return y_n2, y_n3, y_n4
        
# funcion para calcular x
def calcular_x(v, e1, e2, w0, w1, w2, e3, w3):
    return(v*w0 + e1*w1 + e2*w2 + e3*w3)

# funcion para calcular y
def calcular_y(x):
    return(1/(1 + math.exp(-x)))

def main():
    e1 = [0, 0, 1, 1]
    e2 = [0, 1, 0, 1]
    sd = [0, 1, 1, 0]

    v = 1

    w0 = 0.9
    w1 = 0.7
    w2 = 0.5
    w3 = 0.3
    w4 = -0.9
    w5 = -1
    w6 = 0.8
    w7 = 0.35
    w8 = 0.1
    w9 = -0.23
    w10 = -0.79
    w11 = 0.56
    w12 = 0.6
    w13 = -0.6
    w14 = 0.22
    w15 = -0.22
    w16 = -0.56
    w17 = 0.31
    w18 = -0.32

    for cont in range(4):
        # cantidad de neuronas en capa de entrada
        ne = 2
        # cantidad de neuronas en capa oculta
        no = 3

        
        y_n0, y_n1 = calculos_entradas(ne, v, e1[cont], e2[cont], w0, w1, w2, w3, w4, w5)

        y_n2, y_n3, y_n4 = calculos_ocultas(no, v, y_n0, y_n1, w6, w7, w8, w9, w10, w11, w12, w13, w14)

        x = calcular_x(v, y_n2, y_n3, w15, w16, w17, y_n4, w18)
        y = calcular_y(x)

        print(f"La salida real para e1 = {e1[cont]} y e2 = {e2[cont]} es {y}")

        error = sd[cont] - y

        print(f"El error es {error}")

if __name__ == '__main__':
    main()