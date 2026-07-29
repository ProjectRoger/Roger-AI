# Roger Lesson 9

network = {
    "input": 4,
    "hidden_1": 5,
    "hidden_2": 3,
    "output": 1
}

print("Roger Network Architecture:")
print("-" * 30)

for layer, neurons in network.items():
    print(f"Layer: {layer}, Neurons: {neurons}")