def array_reverse(arr):
    """
    Reverses elements in a given list without using built in list.reverse() method

    Parameters:
    arr (List): An array of items to be reversed.

    Returns:
    List: A new list with the elements in reverse order

    """
    output = []

    idx = len(arr) - 1

    while idx >= 0:
        output.append(arr[idx])
        idx -= 1

    return output
