class Calculator:

    def __init__(self):
        self.result = 0

    def add(self, input):
        self.result += input
        return self

    def subtract(self, input):
        self.result -= input
        return self

    def out(self):
        return self.result