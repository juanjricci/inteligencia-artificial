import time


inicio = time.time()
x = []
for i in range(1000000):
    x.append(1 + i)
final = time.time()
print({final - inicio})

inicio = time.time()
x = []
for i in range(1000000):
    x += [1 + i]
final = time.time()
print({final - inicio})

inicio = time.time()
x = []
for i in range(1000000):
    x.extend([1 + i])
final = time.time()
print({final - inicio})