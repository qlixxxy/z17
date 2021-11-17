import math

def sin(x, e):
    approximate = x
    n = 1
    sin_math = (((-1) ** n) * x ** ((2 * n) + 1)) / math.factorial((2 * n) + 1)
    while  abs(sin_math) > e:
        approximate += sin_math
        n += 1
        sin_math = (((-1) ** n) * x ** ((2 * n) + 1)) / math.factorial((2 * n) + 1)
    return approximate


print(sin(0.8, 0.001))
