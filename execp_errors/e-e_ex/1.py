def safe_divide(a, b):
    """
    Divide a by b. Handle ZeroDivisionError.
    Return result or error message.
    """

    try:
        return a / b

    except ZeroDivisionError:
        print("please don't divide by zero")
    return None


# Test
print(safe_divide(10, 2))
print(safe_divide(10, 0))