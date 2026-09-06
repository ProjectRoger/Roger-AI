def matrix_vector_multiply(matrix, vector):
    if len(matrix[0]) != len(vector):
        raise ValueError("Dimensions do not match")

    result = []

    for row in matrix:

        total = 0

        for weight, value in zip(row, vector):
            total += weight * value

        result.append(total)

    return result

W = [
    [0.1, 0.2, 0.3],
    [0.4, 0.5, 0.6],
    [0.7, 0.8, 0.9]
]

X = [5, 10, 15]

output = matrix_vector_multiply(W, X)

print(output)