import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def lcm_range(n):
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result

print("LCM 1..20 =", lcm_range(20))
print("LCM 1..200 =", lcm_range(200))
print("LCM 1..2000 =", lcm_range(2000)) 