import sympy as sp

def gradient(x):
    a = sp.symbols('a')
    function = a ** 2 + 4 * a + 2
    grad=sp.diff(function, a)
    return float(grad.subs(a,x))

function ="( x^2+4x+2 )"
print("Function= ",function)

import numpy as np
x=float(np.random.uniform(1,100))
print("{x} first value=",x)

learning_rate = 0.1

for epoch in range(1,1000):
    grad = gradient(x)
    x = x - (grad * learning_rate)
    if abs(grad) < 0.0001:
        print("\nFunction MİN Found:")
        print("{x} last value=",np.round(x))
        print("Epoch number: ", epoch)
        break

#MOMENTUM_ADD

import sympy as sp

def gradient(x):
    a = sp.symbols('a')
    function = a ** 2 + 4 * a + 2
    grad=sp.diff(function, a)
    return float(grad.subs(a,x))

function ="( x^2+4x+2 )"
print("Function= ",function)

import numpy as np
x=float(np.random.uniform(1,100))
print("{x} first value=",x)

learning_rate = 0.1
beta=0.9
momentum=0.0

for epoch in range(1,1000):
    grad = gradient(x)
    momentum = (momentum * beta) + ((1.0 - beta) * grad)
    x = x - (momentum * learning_rate)
    if abs(grad) < 0.0001:
        print("\nFunction MİN Found:")
        print("{x} last value=",np.round(x))
        print("Epoch number: ", epoch)
        break

#ADAM_OPTIMIZER_ADD

import sympy as sp

def gradient(x):
    a = sp.symbols('a')
    function = a ** 2 + 4 * a + 2
    grad=sp.diff(function, a)
    return float(grad.subs(a,x))

function ="( x^2+4x+2 )"
print("Function= ",function)

import numpy as np
x=float(np.random.uniform(1,100))
print("{x} first value=",x)

learning_rate = 0.1
beta1=0.9
beta2=0.999
momentum=0.0 #Gradient direction
variance=0.0 #Gradient size
epsilon=0.00000001 #Undefined prevent

for epoch in range(1,1000):
    grad = gradient(x)
    momentum = (momentum * beta1) + ((1.0 - beta1) * grad)
    variance=(variance*beta2)+((1.0-beta2)*(grad**2))
    momentum_adjusted=momentum/(1.0-beta1**epoch)
    variance_adjusted=variance/(1.0-beta2**epoch)
    x = x - (momentum_adjusted * learning_rate)/(variance_adjusted**0.5+epsilon)
    if abs(grad) < 0.0001:
        print("\nFunction MİN Found:")
        print("{x} last value=",np.round(x))
        print("Epoch number: ", epoch)
        break