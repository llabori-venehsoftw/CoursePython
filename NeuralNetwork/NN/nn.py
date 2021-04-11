#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 01:14:08 2021

@author: llabori
"""

from data import get_mnist
import numpy as ny
import matplotlib.pyplot as plt

"""
w = weights, b = bias, i = input, h = hidden, o = output, l = label
e.g = w_i_h = weights from input layer to hidden layer 
"""
images, labels = get_mnist()
w_i_h = ny.random.uniform(-0.5, 0.5, (20, 784))
w_h_o = ny.random.uniform(-0.5, 0.5, (10,20))
b_i_h = ny.zeros((20,1))
b_h_o = ny.zeros((10,1))
learn_rate = 0.01
nr_correct = 0
epochs = 3

for epochs in range(epochs):
    for img, l in zip(images, labels):
        img.shape += (1,)
        l.shape += (1,)
        # Forward propagation input to hidden
        h_pre = b_i_h + w_i_h @ img
        h = 1 / (1 + ny.exp(-h_pre)) 
        # Forward propagation hoidden to output
        o_pre = b_h_o + w_h_o @ h
        o = 1 / (1 + ny.exp(-o_pre))
        
        # Cost / Error calculation
        e = 1 / len(o) * ny.sum((0 - l)**2, axis = 0)
        nr_correct += int(ny.argmax(o) == ny.argmax(l))
        
        # Backpropagation output -> hidden (cost function derivative)
        delta_o = o - l
        w_h_o += -learn_rate * delta_o @ ny.transpose(h)
        b_h_o += -learn_rate * delta_o
        
        # Backpropagation hidden -> input (activation function derivative)
        delta_h = ny.transpose(w_h_o) @ delta_o * (h - (1 - h))
        w_i_h += -learn_rate * delta_h @ ny.transpose(img)
        b_i_h += -learn_rate * delta_h
        
        # Show accuracy for this epoch
        print(f"Acc: {round((nr_correct / images.shape[0]) * 100, 2)}%")
        nr_correct = 0
        
# Show the result
while True:
    index = int(input("Enter a number ( 0  59999): ") )
    img = images[index]
    plt.imshow(img.reshape(28, 28), cmap="Greys")
    
    img.shape += (1,)
    # Forward propagation inpu -> hidden
    h_pre = b_i_h + w_i_h @ img.reshape(784, 1)
    h = 1 / (1 + ny.exp(-h_pre))
    # Forward propagation hidden -> output
    o_pre = b_h_o + w_h_o @ h
    o = 1 / (1 + ny.exp(-o_pre))
    plt.title(f"Subscribe if its a {o.argmax()} :)")
    plt.show()