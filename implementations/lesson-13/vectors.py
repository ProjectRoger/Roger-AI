def dot_product(a,b): 
    if len(a) != len(b):
        raise ValueError("vectors must have same length")

    result = 0

    for x,y in zip(a,b):
        result += x*y
    
    return result

x = [1, 2, 3]
y = [0.8, 0.5, 0.2]

result = dot_product(x,y)

print(result)