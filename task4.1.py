import math

pi = 4

interation = 1000000
for i in range(1, interation + 1):
    pi += ((-1) ** i) * (4 / (2 * i + 1))   
print(pi)
print("math.pi =", math.pi) 

