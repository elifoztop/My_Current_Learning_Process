import numpy as np
import math
import sys

inputs=np.array([[0,0],[0,1],[1,0],[1,1]]) #4 example 2 input
weights=np.random.rand(2)
bias=np.random.rand()
real=[0,0,0,1]
learning_rate=0.1
epochs=0
stop=0


def sigmoid(z):
    return 1/(1+math.exp(-z))

while epochs < 100000:
    epochs+=1
    stop=0
    outputs=np.array([-1.0,-1.0,-1.0,-1.0]) #float array
    for t in range(4):
        product1 = np.dot(inputs[t][0], weights[0])
        product2 = np.dot(inputs[t][1], weights[1])
        argument = product1 + product2 + bias
        output = sigmoid(argument)
        mistake =real[t]-output #real-estimation
        outputs[t] = output
        if abs(mistake) < 0.01: #abs=||
            stop = stop + 1
            if stop == 4:
                print("Weights: ", weights)
                print("Bias:", bias)
                print("Again_num:",epochs)
                print("Inputs:\n",inputs)
                print("Outputs: ",np.round(outputs))
                sys.exit()
        weights[0] = weights[0] + (mistake * learning_rate * inputs[t][0])
        weights[1] = weights[1] + (mistake * learning_rate * inputs[t][1])
        bias = bias + (mistake * learning_rate)


