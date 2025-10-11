def sum_numbers(lst):
    """
    Sum all numbers in list.
    Skip non-numeric items and count errors.
    Return tuple: (sum, error_count)
    """
    # Your code here

    sum = 0
    error_count = 0
    for item in lst:
        try:
            sum += item
        except TypeError :
            error_count += 1

    return (sum, error_count)




# Test
print(sum_numbers([1, 2, 3, 4]))           # (10, 0)
print(sum_numbers([1, "a", 3, None, 5]))   # (9, 2)