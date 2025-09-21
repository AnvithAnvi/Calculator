import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def power(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot modulo by zero.")
    return a % b

def floor_divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot floor-divide by zero.")
    return a // b

def absolute(x):
    return abs(x)

def sqrt(x):
    if x < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(x)