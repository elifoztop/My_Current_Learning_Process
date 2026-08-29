#inputs=[temperature, humidity]
#output=Can we go outside?(Yes=1 , No=0)

import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

data=np.array([
    [22, 40],
    [28, 50],
    [15, 35],
    [20, 45],
    [26, 55],
    [32, 80],
    [38, 70],
    [10, 90],
    [5,  85],
    [35, 75],
])

inputs = np.array([
    # [temperature,humidity]
    [22, 40],
    [28, 50],
    [15, 35],
    [20, 45],
    [26, 55],
    [32, 80],
    [38, 70],
    [10, 90],
    [5,  85],
    [35, 75],
]) / 100.0 #normalization

real = np.array([
    [1],
    [1],
    [1],
    [1],
    [1],
    [0],
    [0],
    [0],
    [0],
    [0],
])

learning_rate=0.1

weights=np.random.rand(inputs.shape[1],1)
bias=np.random.rand(1)

for epoch in range(1,100000000):
    z=np.dot(inputs,weights)+bias
    outputs=sigmoid(z)

    mse=np.mean((real-outputs)**2)

    if epoch % 10000 == 0:
        print(f"Epoch {epoch} | Mistake: {mse:.6f}")

    if mse < 0.0001:
        print("Weights:\n ", weights)
        print("Bias:", bias)
        print("Again_num:", epoch)
        print("Inputs:\n", data)
        print("Outputs:\n", np.round(outputs))
        break

    error_signal=(real-outputs)*outputs*(1-outputs) #mistake*sigmoid_derivative(outputs)

    weights_gradient = np.dot(inputs.T, error_signal)
    bias_gradient = np.sum(error_signal)

    weights+= weights_gradient * learning_rate
    bias+= bias_gradient * learning_rate

print("Traning data processed!")
again=1
while again==1:
    temperature = int(input("Air temperature:"))
    humidity = int(input("Air humidity:"))
    test = np.array([[temperature, humidity]]) / 100
    t_output = sigmoid(np.dot(test, weights) + bias)
    print("Can we go outside?")
    if np.round(t_output) < 0.5:
        print("NO")
    else:
        print("YES")
    again = int(input("Try again? (Yes=1/No=0): "))










