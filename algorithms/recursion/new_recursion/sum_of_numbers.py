"""
Calculate the sum of list of numbers.
"""

from typing import List


def sum_of_numbers(list_: List[int]) -> int:
    s = 0
    for num in list_:
        s += num

    return s


def sum_of_numbers_recursion(list_: List[int]) -> int:
    s = 0

    if not list_:
        s = 0
    elif len(list_) == 1:
        s += list_[0]
    else:
        s += list_[0] + sum_of_numbers_recursion(list_[1:])

    return s


if __name__ == '__main__':
    # structure of lists items: ([values to sum], answer)
    lists = (
        ([1, 2, 3], 6),
        ([], 0),
        ([-4, 4, 0], 0),
        ([2, 2], 4),
        ([8, -4, 4, 1], 9),
    )

    for item in lists:
        assert sum_of_numbers(item[0]) == sum_of_numbers_recursion(item[0]) == item[1]
