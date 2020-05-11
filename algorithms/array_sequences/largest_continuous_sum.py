x = [1, 2, -3, -5, 2, 3, 1, 9, -10, -2, 1]
y = [1, 2, -1, 3, 4, 10, 10, -10, -1]


def largest_continuous_sum(items: list) -> int:
    """
    The function is designed to find the largest continuous sum of numbers
    :param items: is a list of integers in random order
    :return: the largest continuous sum of numbers
    """
    assert isinstance(items, list), "items should be list"
    assert len(items) > 0, "items should not be empty"
    assert len([i for i in items if isinstance(i, int)]) == len(items), "items should be list of integers"

    largest_sum = items[0]
    for i in range(len(items)):
        s = 0
        for j in range(i, len(items)):
            s += items[j]
            if largest_sum <= s:
                largest_sum = s
    return largest_sum


if __name__ == '__main__':
    print(largest_continuous_sum(x))
    print(largest_continuous_sum(y))
    print(largest_continuous_sum([-5, -3, 1]))
