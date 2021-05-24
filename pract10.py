def bucketsort(arr, k):
    """
    Sort function to get sorted array.

    >>> bucketsort([3, 2, 1], 16)
    [1, 2, 3]

    >>> bucketsort([], 16)
    []

    >>> bucketsort([3, 2, 1], 2)
    Traceback (most recent call last):
      ...
    IndexError: list index out of range

    >>> bucketsort([2, 1, 3], 2)
    Traceback (most recent call last):
      ...
    IndexError: list index out of range

    :param arr: array to be sorted
    :param k: ???
    :return: sorted array
    """
    counts = [0] * k
    for x in arr:
        counts[x] += 1

    sorted_arr = []
    for i, count in enumerate(counts):
        sorted_arr.extend([i] * count)

    return sorted_arr
