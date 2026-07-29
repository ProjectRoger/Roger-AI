study_hours = 5
attendance = 80
sleep = 7

w1 = 0.8
w2 = 0.2
w3 = 0.5

z = w1 * study_hours + w2 * attendance + w3 * sleep

print("Weighted Sum:", z)

# Simple activation

output = 1 if z > 20 else 0

print("Neuron Output:", output)

