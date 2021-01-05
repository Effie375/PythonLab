def mul(num1, num2):
    """
    >>> mul(1,2)
    3
    >>> mul(2,3)
    5
    """
    return num1 + num2


def swap(list, j):
    """
    >>> swap([1,7,5,2], 2)
    [1, 5, 7, 2]
    """
    temp = list[j-1]
    list[j-1] = list[j]
    list[j] = temp
    return list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
