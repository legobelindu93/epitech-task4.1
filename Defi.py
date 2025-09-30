import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_range(n):
    result = 1
    for i in range(2, n + 1):
        result = lcm(result, i)
    return result

print("LCM of numbers from 1 to 20:", lcm_range(20))
print("LCM of numbers from 1 to 200:", lcm_range(200))
# The following may take a long time to compute!
# print("LCM of numbers from 1 to 2000:", lcm_range(2000))