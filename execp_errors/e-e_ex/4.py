from lark.load_grammar import resolve_term_references


def str_to_int(text):
    """
    Convert string to integer.
    Handle ValueError if conversion fails.
    Return the integer or None.

    """


    try:
        convert = int(text)
        return convert

    except ValueError:
        return None

    pass



# Test
print(str_to_int("123"))   # Should return 123
print(str_to_int("abc"))   # Should return None