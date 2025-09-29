"""
Create a calculator that takes two numbers and an operation.
Requirements:
• Take 3 arguments: number1, operation (+, -, *, /), number2
• Perform the calculation and print the result
• Handle division by zero
"""

def calculator(nb1, op, nb2):
    if op == "+":
        return nb1 + nb2
    elif op == "-":
        return nb1 - nb2
    elif op == "*":
        return nb1 * nb2
    elif op == "/":
        if nb2 == 0:
            return "Error: Division by zero"
        return nb1 / nb2
    else:
        return "Error: Invalid operation"

if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        description="Create a calculator that takes two numbers and an operation."
    )
    parser.add_argument("number1", type=float, help="The first number")
    parser.add_argument("operation", type=str, help="The operation (+, -, *, /)")
    parser.add_argument("number2", type=float, help="The second number")

    args = parser.parse_args()

    number1 = args.number1
    number2 = args.number2
    operation = args.operation

    result = calculator(number1, operation, number2)
    print("Result:", result)
    sys.exit(0)
