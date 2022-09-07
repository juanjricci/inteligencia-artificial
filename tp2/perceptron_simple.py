import random
import math
import matplotlib.pyplot as plt 


lista_iteraciones = []
lista_error0 = []
lista_error1 = []
lista_error2 = []
lista_error3 = []

lista_pesos0 = []
lista_pesos1 = []
lista_pesos2 = []

print("\nPERCEPTRON SIMPLE")
print("-----------------")
print("Como desea que se comporte el perceptron? ")
print("\t1. Compuerta OR.\n\t2. Compuerta AND.")
selected = int(input("Ingrese la opcion deseada: "))

e0 = 1
# tabla logica
e1 = [0, 0, 1, 1]
e2 = [0, 1, 0, 1]
if selected == 1:
    s = [0 ,1 ,1, 1]
elif selected == 2:
    s = [0 ,0 ,0, 1]

error0 = 1
error1 = 1
error2 = 1
error3 = 1

# pesos sinopticos
w0 = random.uniform(-1, 1)
w1 = random.uniform(-1, 1)
w2 = random.uniform(-1, 1)

# w0 = 0.9
# w1 = 0.66
# w2 = -0.2

print(f"\nPesos sinopticos iniciales")
print(f"w0 = {w0}")
print(f"w1 = {w1}")
print(f"w2 = {w2}")

salida = 0
learning = True
i = 0
learning_rate = 0.1

while learning == True:
    #print(f"Iteracion #{i} ---> {w0}/{w1}/{w2}")
    i += 1
    # print(f"Iteracion {i}")
    learning = False
    lista_iteraciones.append(i)
    lista_pesos0.append(w0)
    lista_pesos1.append(w1)
    lista_pesos2.append(w2)
    
    # if i == 5:
    #     break
    for cont in range(4):
        # print(f"Renglon {cont}")
        #print(f"e1 = {e1[cont]} -- e2 = {e2[cont]} -- s = {s[cont]}")
        x = e0*w0 + e1[cont]*w1 + e2[cont]*w2
        #print(f"x = {x}")
        y = 1/(1+math.exp(-x))
        #print(f"y = {y}")
        error = s[cont] - y
        exec(f'error{cont} = error')
        exec(f'lista_error{cont}.append(error{cont})')

        if abs(error0) > 0.1 or abs(error1) > 0.1 or abs(error2) > 0.1 or abs(error3) > 0.1:

            learning = True

            delta = y*(1-y)*error
            #print(f"delta = {delta}")
            
            dw0 = learning_rate * e0 * delta
            #print(f"dw0 = {dw0}")
            dw1 = learning_rate * e1[cont] * delta
            #print(f"dw1 = {dw1}")
            dw2 = learning_rate * e2[cont] * delta
            #print(f"dw2 = {dw2}")
            # nuevos pesos sinopticos
            w0 = w0 + dw0
            # print(f"w0 = {w0}")
            w1 = w1 + dw1
            # print(f"w1 = {w1}")
            w2 = w2 + dw2
            # print(f"w2 = {w2}")
            
    # if i == 2:
    #     break

    if learning == False:
        break

print(f"\nIteraciones = {i}\n")
print("Pesos sinopticos finales")
print(f"w0 = {w0}")
print(f"w1 = {w1}")
print(f"w2 = {w2}")
print("\nTabla logica resultante:\n")
print("\t| e1 | e2 | s |")
print("\t---------------")
for cont in range(0,4):
    x = e0*w0 + e1[cont]*w1 + e2[cont]*w2
    y = 1/(1+math.exp(-x))
    if y > 0.5:
        salida = 1
    else:
        salida = 0
    print(f"\t| {e1[cont]}  | {e2[cont]}  | {salida} |")


# Menu para graficar
while True:
    # print(f"Error1: {error0}")
    # print(f"Error2: {error1}")
    # print(f"Error3: {error2}")
    # print(f"Error4: {error3}")
    print("Que desea graficar?\n")
    print("\t1. Grafico de errores.")
    print("\t2. Grafico de pesos sinopticos.")
    print("\t3. Salir.")
    selected = int(input("Ingrese la opcion deseada: "))
    if selected == 1:
        plt.xlabel("Iteraciones")
        plt.ylabel("Errores")
        plt.title("GRÁFICO DE ERRORES")
        plt.axhline(y=0, color='black', linestyle='-')
        plt.plot(lista_iteraciones, lista_error0)
        plt.plot(lista_iteraciones, lista_error1)
        plt.plot(lista_iteraciones, lista_error2)
        plt.plot(lista_iteraciones, lista_error3)
        plt.show()
    elif selected == 2:
        plt.xlabel("Iteraciones")
        plt.ylabel("Pesos")
        plt.title("GRÁFICO DE PESOS SINOPTICOS")
        plt.axhline(y=0, color='black', linestyle='-')
        plt.plot(lista_iteraciones, lista_pesos0)
        plt.plot(lista_iteraciones, lista_pesos1)
        plt.plot(lista_iteraciones, lista_pesos2)
        plt.show()
    elif selected == 3:
        break
    else: 
        print("Ingrese una opcion valida.")
#input("Presione ENTER para continuar...")