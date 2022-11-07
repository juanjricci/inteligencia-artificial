# xor_muy_simpleANDA
import tensorflow as tf
import time
import numpy as np
import matplotlib.pyplot as plt
import cv2



tf.compat.v1.disable_eager_execution()

path = f'angry.jpg'
print(f"Using image from {path}")

img = cv2.imread(path)
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rows, cols = grey.shape

imgarray = [1]

for i in range(rows):
    for j in range(cols):
        imgarray.append(img[i, j][0])

errors=[]

XOR_X = [[0,0],[0,1],[1,0],[1,1]]
XOR_Y = [[0],[1],[1],[0]]

x_ = tf.compat.v1.placeholder(tf.float32, shape=[4,2], name = 'x-input')
y_ = tf.compat.v1.placeholder(tf.float32, shape=[4,1], name = 'y-input')

# 2,3: 2 entradas para cada una de las tres neuronas en capa oculta
# 3,1: 3 entradas para una neurona en capa oculta

Pesos1 = tf.Variable(tf.random.uniform([2,3], -1, 1), name = "Pesos1")
Bias1 = tf.Variable(tf.random.uniform([3],-1,1), name = "Bias1")
Pesos2 = tf.Variable(tf.random.uniform([3,1], -1, 1), name = "Pesos2")
Bias2 = tf.Variable(tf.random.uniform([1],-1,1), name = "Bias2")

A = tf.sigmoid(tf.matmul(x_, Pesos1) + Bias1)
Salida = tf.sigmoid(tf.matmul(A, Pesos2) + Bias2)

#Costo=tf.reduce_mean(abs(y_-Salida))
Costo=tf.reduce_mean(input_tensor=(y_*tf.math.log(Salida)+((1 - y_)* tf.math.log(1.0-Salida)))*-1)

train_step = tf.compat.v1.train.GradientDescentOptimizer(.9).minimize(Costo)

init = tf.compat.v1.global_variables_initializer()
sess = tf.compat.v1.Session()
sess.run(init)

t_start = time.time()
for i in range(801):
    sess.run(train_step, feed_dict={x_: XOR_X, y_: XOR_Y})
    errors.append(sess.run(Costo, feed_dict={x_: XOR_X, y_: XOR_Y}))
t_end = time.time()

print ("Serie ", i)
print ("Salida ", sess.run(Salida, feed_dict={x_: XOR_X, y_: XOR_Y}))
print('Pesos1 ', sess.run(Pesos1))
print ('Bias1 ', sess.run(Bias1))
print('Pesos2 ', sess.run(Pesos2))
print('Bias2 ', sess.run(Bias2))
print('Costo ', sess.run(Costo, feed_dict={x_: XOR_X, y_: XOR_Y}))
print('Tiempo transcurrido ', t_end - t_start)
# lista_iteraciones = [i for i in range(801)]
# plt.plot(lista_iteraciones, errors)
plt.plot([np.mean(errors[i-50:i]) for i in range(len(errors))])
plt.show()