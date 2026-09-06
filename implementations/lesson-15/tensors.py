import numpy as np

scalar = np.array(5)

vector = np.array([1, 2, 3])

matrix = np.array([
    [1, 2, 3], 
    [4, 5, 6]
    ])

tensor_3d = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print("Scalar:", scalar)
print("Vector:", vector)
print("Matrix:", matrix)
print("3D Tensor:", tensor_3d)


# Shape

print("Scalar shape:", scalar.shape)
print("Vector shape:", vector.shape)
print("Matrix shape:", matrix.shape)
print("3D tensor shape:", tensor_3d.shape)

# Dimensions

print("Scalar ndim:", scalar.ndim)
print("Vector ndim:", vector.ndim)
print("Matrix ndim:", matrix.ndim)
print("3D tensor ndim:", tensor_3d.ndim)

# Size

print(scalar.size)
print(vector.size)
print(matrix.size)
print(tensor_3d.size)


# Matrix Multplication

print("Matrix Multiplication")

W = np.array([
    [0.1, 0.2, 0.3],
    [0.4, 0.5, 0.6],
    [0.7, 0.8, 0.9],
    [0.2, 0.4, 0.6]
])

X = np.array([5, 80, 7])

result = W @ X

print(result)



# Manual Matrix Multiplication

print("Manual Matrix Multiplication")

def matrix_vector_multiply(matrix, vector):

    if len(matrix[0]) != len(vector):
        raise ValueError("Matrix columns must match vector size.")

    result = 0 

    for row in matrix:

        total = 0
        for weight, value in zip(row, vector):
            total += weight * value

        result = np.append(total, result)

    return result


manual_result = matrix_vector_multiply(W, X)
numpy_result = W @ X

print("Manual:", manual_result)
print("NumPy:", numpy_result)


# Broadcasting

print("Broadcasting")

X = np.array([[1, 2, 3], [4, 5, 6]])

bias = np.array([10, 20, 30])

result = X + bias

print(result)


# Complete Tiny Neuarl Network Layer

print("Complete Tiny Neural Network Layer")

X = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9],[10, 11, 12]])

W = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])

b = np.array([10, 20])

z = X @ W.T + b

print(z)