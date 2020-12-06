def factorial(input):
    return input * factorial(input - 1) if input > 1 else 1