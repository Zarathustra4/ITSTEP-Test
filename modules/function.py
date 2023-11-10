def foo():
    print("Somthing...")

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def prod(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b\


def factorial(n: int):
    if n == 0:
        return 0
    return n * factorial(n - 1)

def inf_loop():
    print("Bla-Bla-Bla")
    while True:
        print("infinity")