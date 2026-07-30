import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def tanh(x):
    return math.tanh(x)

def relu(x):
    return max(0, x)

def gelu_approx(x):
    return 0.5 * x * (1 + math.tanh(math.sqrt(2 / math.pi) * (x + 0.044715 * x ** 3)))


values = [-3, -1, 0, 1, 3]

for v in values:
    print(f"x: {v}")
    print(f"Sigmoid: {sigmoid(v):.4f}")
    print(f"Tanh: {tanh(v):.4f}")
    print(f"ReLU: {relu(v):.4f}")
    print(f"GELU: {gelu_approx(v):.4f}")
    print("-" * 30)