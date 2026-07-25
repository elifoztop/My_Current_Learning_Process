import numpy as np
import math

inputs=np.random.rand(3)
print(inputs)

weights=np.random.rand(3)
print(weights)

bias=np.random.rand()
print(bias)

product_sum=0
for i in range(3):
    product_sum+=inputs[i]*weights[i]
print(product_sum)

argument=product_sum+bias
print(argument)

def sigmoid(x):
    return 1/(1+math.exp(-x))

output=sigmoid(argument)
print(output)