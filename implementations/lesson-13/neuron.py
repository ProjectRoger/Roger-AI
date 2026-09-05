def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError("vectors must have same length")

    return sum(x * y for x, y in zip(a, b))

def relu(x):
    return max(0,x)

def nueuron(x, weights, bias):
    z = dot_product(x, weights) + bias
    return relu(z)

x = [5,80,7]    
weights = [0.2, 0.5, 0.1]
bias = 2

output = nueuron(x, weights, bias)

print("Neuron output:", output)
