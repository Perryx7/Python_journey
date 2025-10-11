

def validate_age(age):
    """
    Check if age is valid (0-120).
    Raise ValueError with message if invalid.
    Return True if valid.
    """
    # Your code here
    if age in range(0, 120):
        return True
    else:
        raise ValueError("Invalid age")
    pass

# Test
try:
    print(validate_age(25))    # Should return True
    print(validate_age(-5))    # Should raise ValueError
except ValueError as e:
    print(e)