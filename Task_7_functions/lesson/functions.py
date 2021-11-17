arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return func_fib(n - 1) + func_fib(n - 2)

print(func_fib(996))
