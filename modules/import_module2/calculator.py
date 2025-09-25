# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b


# This block only runs if you execute calculator.py directly
if __name__ == '__main__':
    print("Testing calculator functions inside calculator.py")
    print("Add: 2 + 3 =", add(2, 3))
    print("Subtract: 7 - 4 =", subtract(7, 4))
    print("Multiply: 3 * 5 =", multiply(3, 5))
    print("Divide: 10 / 2 =", divide(10, 2))
    print("Power: 2 ^ 4 =", power(2, 4))
