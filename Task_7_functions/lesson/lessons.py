from random import randint
def names(a):
    return f'Hello, {a}'

arr = ['Sanya', 'Leha', 'Zhekich', 'Romych', 'Vasya']

for i in arr:
    print(names(i))

def get_array(n, m):
    matrix = [[randint(0, 10) for i in range(n)] for j in range(m)]
    return matrix


def print_arr(matrix):
    print(matrix)


def sum(matrix):
    sum = 0 
    for i in matrix:
        for j in i:
            sum += j
    return sum


def max(matrix):
    max = 0
    for i in matrix:
        for j in i:
            if j > max:
                max = j
    return max

def min(matrix):
    min = 0
    for i in matrix:
        for j in i:
            if j < min:
                min = j
    return min

arr_matrix = get_array(5, 5)
print_arr(arr_matrix)
print(sum(arr_matrix))
print(max(arr_matrix))
print(min(arr_matrix))

def fact():
    n = int(input('Введи n'))
    result = 1
    for i in range(1, n):
        result *= i
    return result    

print(fact())

def matrix_init(n, **kwargs):
  matrix = [[randint(kwargs['random_from'], kwargs['random_to']) for x in range(n)] for i in range(n)]
  return matrix

print(matrix_init(3, random_from=1, random_to=9))