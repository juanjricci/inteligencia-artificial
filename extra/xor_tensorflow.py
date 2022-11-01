# xor_muy_simpleANDA
import tensorflow as tf
import time
import numpy as np
import matplotlib.pyplot as plt

errors=[]

XOR_X = [[0,0],[0,1],[1,0],[1,1]]
XOR_Y = [[0],[1],[1],[0]]

x_ = tf.placeholder(tf.float32, shape=[4,2], name = 'x-input')
y_ = tf.placeholder(tf.float32, shape=[4,1], name = 'y-input')

# 2,3: 2 entradas para cada una de las tres neuronas en capa oculta
# 3,1: 3 entradas para una neurona en capa oculta

Pesos1 = tf.Variable(tf.random_uniform([2,3], -1, 1), name = "Pesos1")
Bias1 = tf.Variable(tf.random_uniform([3],-1,1), name = "Bias1")
Pesos2 = tf.Variable(tf.random_uniform([3,1], -1, 1), name = "Pesos2")
Bias2 = tf.Variable(tf.random_uniform([1],-1,1), name = "Bias2")

A = tf.sigmoid(tf.matmul(x_, Pesos1) + Bias1)
Salida = tf.sigmoid(tf.matmul(A, Pesos2) + Bias2)

#Costo=tf.reduce_mean(abs(y_-Salida))
Costo=tf.reduce_mean((y_*tf.log(Salida)+((1 - y_)* tf.log(1.0-Salida)))*-1)

train_step = tf.train.GradientDescentOptimizer(.9).minimize(Costo)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

t_start = time.clock()
for i in range(801):
    sess.run(train_step, feed_dict={x_: XOR_X, y_: XOR_Y})
    errors.append(sess.run(Costo, feed_dict={x_: XOR_X, y_: XOR_Y}))
t_end = time.clock()

print ("Serie ", i)
print ("Salida ", sess.run(Salida, feed_dict={x_: XOR_X, y_: XOR_Y}))
print('Pesos1 ', sess.run(Pesos1))
print ('Bias1 ', sess.run(Bias1))
print('Pesos2 ', sess.run(Pesos2))
print('Bias2 ', sess.run(Bias2))
print('Costo ', sess.run(Costo, feed_dict={x_: XOR_X, y_: XOR_Y}))
print('Tiempo transcurrido ', t_end - t_start)
plt.plot([np.mean(errors[i-50:i]) for i in range(len(errors))])
plt.show()