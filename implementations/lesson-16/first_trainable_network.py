import numpy as np

# Initialize parameters

np.random.seed(42)

X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5]
], dtype=float)

y = np.array([
    [35],
    [45],
    [55],
    [65],
    [75]
], dtype=float)

# Creating the weights

W1 = np.random.randn(1,4) * 0.1
b1 = np.zeros((1,4))

W2 = np.random.randn(4,1) * 0.1
b2 = np.zeros((1,1))

print(W1.shape)
print(b1.shape)

print(W2.shape)
print(b2.shape)

def relu(x):
    return np.maximum(0, x)

# Forward pass

for epoch in range(10000):

    Z1 = X @ W1 + b1
    A1 = relu(Z1)

    Z2 = A1 @ W2 + b2

    prediction = Z2

    # print("X:", X.shape)
    # print("Z1:", Z1.shape)
    # print("A1:", A1.shape)
    # print("Z2:", Z2.shape)
    # print("Prediction:", prediction.shape)

    # Calculating loss

    loss = np.mean((prediction - y) ** 2)

    print("Loss:", loss)

    # Starting at the loss

    dZ2 = 2 * (prediction - y) / len(X)

    # Gradient for W2

    dW2 = A1.T @ dZ2
    db2 = np.sum(dZ2, axis=0, keepdims=True)

    # Moving backward through the second layer

    dA1 = dZ2 @ W2.T

    # Back through ReLU

    dZ1 = dA1 * (Z1 > 0)

    # Gradient for W1

    dW1 = X.T @ dZ1
    db1 = np.sum(dZ1, axis=0, keepdims=True)

    # Updating the parameters

    learning_rate = 0.001

    W2 = W2 - learning_rate * dW2
    b2 = b2 - learning_rate * db2

    W1 = W1 - learning_rate * dW1
    b1 = b1 - learning_rate * db1

    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {loss}")

# Testing the network

Z1 = X @ W1 + b1
A1 = relu(Z1)
prediction = A1 @ W2 + b2

print(prediction)

new_X = np.array([
    [6],
    [7],
    [10]
], dtype=float)

Z1 = new_X @ W1 + b1
A1 = relu(Z1)
new_prediction = A1 @ W2 + b2

print(new_prediction)