def get_item(lst, index):
    """
    Return item at index from list.
    Handle IndexError if index is out of range.
    """
    # Your code here


    try:
        return lst[index]
    #for index error
    except IndexError:
        raise IndexError("Index out of range")


# Test
numbers = [1, 2, 3, 4, 5]
print(get_item(numbers, 2))   # Should return 3
print(get_item(numbers, 10))  # Should return error message