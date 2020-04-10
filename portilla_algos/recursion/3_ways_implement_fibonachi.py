def fib_recurs(n) -> int:
    """
    Returns n member of Fibonnaci Sequence
    :param n: number of element in sequence
    :return: the value of n-th element in the sequence
    """
    assert isinstance(n, int), "n should be integer"
    assert n >= 0, "n should be more or equal to 1"
    if n <= 1:
        return 1
    return fib_recurs(n-1) + fib_recurs(n-2)


def fib_iteration(n) -> int:
    """
    Returns n member of Fibonnaci Sequence
    :param n: number of element in sequence
    :return: the value of n-th element in the sequence
    """
    assert isinstance(n, int), "n should be integer"
    assert n >= 0, "n should be more or equal to 1"
    if n <= 2:
        return 1
    a = 1
    b = 1
    for i in range(n - 1):
        # without Python internal feature:
        temp = b
        b = a + b
        a = temp
        # with Python internal feature:
        # a, b = b, a+b
    return b


mem_table = {}
def fib_recurs_with_memoization(n) -> int:
    """
    Returns n member of Fibonnaci Sequence
    :param n: number of element in sequence
    :return: the value of n-th element in the sequence
    """
    assert isinstance(n, int), "n should be integer"
    assert n >= 0, "n should be more or equal to 1"
    if n <= 1:
        return 1

    if mem_table.get(n):
        return mem_table[n]

    mem_table[n] = fib_recurs(n-1) + fib_recurs(n-2)
    return mem_table[n]


if __name__ == '__main__':
    print(fib_recurs(7))
    print(fib_iteration(7))
    print(fib_recurs_with_memoization(7))