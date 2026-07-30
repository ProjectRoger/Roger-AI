predictions = [25, 35, 45, 55]
actual = [20, 30, 40, 50]

errors = []

for p, a in zip(predictions, actual):
    error = (p - a) ** 2
    errors.append(error)

mse = sum(errors) / len(errors)

print("Squared Errors:", errors)
print("Mean Squared Error (MSE):", mse)

