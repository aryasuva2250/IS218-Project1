from addition import addition

class Calculator:

    result = 0

    def __init__(self):
        pass

    @staticmethod
    def add(self, a, b):
        self.result = addition(a, b)
        return self.result


