# Roger Lesson 5
# First Learning Machine

hours = [1, 2, 3, 4, 5]

scores = [35, 40, 45, 50, 55]

weight = 1

learning_rate = 0.5

for epoch in range(20):

    total_error = 0

    for x,y in zip(hours, scores):

        prediction = weight * x

        error = y - prediction

        weight += learning_rate * error * 0.01

        total_error += abs(error)

    print(f"Epoch {epoch+1:2d}: Weight = {weight:.4f}, Total Error = {total_error:.2f}")


print("\nFinal Weight:", weight)

print("\nPredictions")

for h in range(1, 6):

    prediction = weight * h

    print(f"{h} hours -> {prediction:.2f}")