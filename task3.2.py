import math



def sum_digits(n):                      # (1) définition d'une fonction appelée "sum_digits" 
    return sum(int(digit) for digit in str(n))   # (2) ce que la fonction fait


print(sum_digits(123456789))
print(sum_digits(112233445566778899))
print(sum_digits(123456789 * 987654321))
           