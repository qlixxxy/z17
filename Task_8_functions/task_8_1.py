arr = [20, 7, 9, 11, 14]

def fact(n):
    fact = 1
    if n % 2 == 0:
        for i in range (2, n + 1, 2):
            fact *= i
    else:
        for i in range (1, n + 1, 2):
            fact *= i
    return fact

for i in arr:
    print(fact(i))
