from calculator import Calculator

def main():
    calculator = Calculator()
    result = calculator.add(4).add(5).subtract(3).out()
    print(result)

main()