def calculator(operation, a, b):
    """
    Perform operation (+, -, *, /) on a and b.
    Handle: ZeroDivisionError, TypeError, ValueError
    Return result or error message with error type.
    """
    try:
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            return a / b
        else:
            # Opération non reconnue
            raise ValueError("Invalid operation")

    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid type (a and b must be numbers)"
    except ValueError as e:
        return f"Error: {e}"

print(calculator("+", 5, 3))      # Should return 8
print(calculator("/", 10, 0))     # Should handle division by zero
print(calculator("*", "5", 3))    # Should handle type error
print(calculator("%", 5, 3))      # Should handle invalid operation

