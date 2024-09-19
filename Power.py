class Power(object):
    defualtExponent = 2
    def __init__(self, exponent=defualtExponent):
        self.exponent = exponent
    def of(self, x):
        if isinstance(self.exponent, int) or x >= 0:
            return x ** self.exponent
        raise ValueError("Fractional powers of negative numbers are imaginary")
def main():
    number0 = Power(3)
    number1 = Power(2)
    print(number1.of(-5))

main()