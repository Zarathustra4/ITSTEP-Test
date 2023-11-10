def foo():
    print("Somthing...")

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def division(a, b):
    if b != 0:
        return a / b

def factorial(n: int):
    result = 1
    for i in range(2, n + 1):
        result *= i

    return result

def inf_loop():
    print("Bla-Bla-Bla")
    while True:
        print("infinity")