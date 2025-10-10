def get_value(dictionary, key):
    """
    Return value for key from dictionary.
    Handle KeyError if key doesn't exist.
    Return "Key not found" on error.
    """
    # Your code here
    try :
        return dictionary[key]
    except KeyError:
        raise KeyError("Key not found")


# Test
person = {"name": "Alice", "age": 30}
print(get_value(person, "name"))    # Should return "Alice"
print(get_value(person, "email"))   # Should return "Key not found"