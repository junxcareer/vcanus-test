from functools import reduce

def factorial_with_reduce(input):
    return reduce(lambda x, y: x * y, range(1, input + 1))

def factorial_with_loop(input):
    result = 1
    for i in range(1, input + 1):
        result * i
    return result
