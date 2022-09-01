import random
import math


e0 = 1
# tabla logica
e1 = [0, 0, 1, 1]
e2 = [0, 1, 0, 1]
s = [0 ,1 ,1, 1]

# pesos sinopticos
w0 = random.uniform(-1, 1)
w1 = random.uniform(-1, 1)
w2 = random.uniform(-1, 1)
print("\nPerceptron Simple")
print("-----------------")
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
    learning = False
    # if i == 2:
    #     break
    for cont in range(0,4):
        #print(f"e1 = {e1[cont]} -- e2 = {e2[cont]} -- s = {s[cont]}")
        x = e0*w0 + e1[cont]*w1 + e2[cont]*w2
        #print(f"x = {x}")
        y = 1/(1+math.exp(-x))
        #print(f"y = {y}")

        if y > 0.5:
            salida = 1
        else:
            salida = 0

        if salida != s[cont]:

            learning = True

            error = s[cont] - y
            #print(f"error = {error}")

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
            #print(f"w0 = {w0}")
            w1 = w1 + dw1
            #print(f"w1 = {w1}")
            w2 = w2 + dw2
            #print(f"dw2 = {w2}")

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