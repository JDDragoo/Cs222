def FahToCel(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    return celsius

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b
        
if __name__ == "__main__":
    print(FahToCel(93))