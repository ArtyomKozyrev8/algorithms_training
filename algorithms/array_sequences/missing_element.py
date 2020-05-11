def find_missing_element(list_one: list, list_two: list) -> int:
    """
    Find the missing element in list_two, the list was created from list_one
    :param list_one: some list which is composed of random positive integers
    :param list_two: list which is made from list_one by removing one random element and shuffle
    :return: the missing element
    """
    assert isinstance(list_one, list), "list_one should be list"
    assert isinstance(list_two, list), "list_two should be list"
    assert len([i for i in list_one if isinstance(i, int)]) == len(list_one), "list_one should be list of integers"
    assert len([i for i in list_two if isinstance(i, int)]) == len(list_two), "list_two should be list of integers"
    assert len([i for i in list_one if i > 0]) == len(list_one), "list_one should be list of positive integers"
    assert len([i for i in list_two if i > 0]) == len(list_two), "list_two should be list of positive integers"

    if len(list_one) == 0:
        return

    if len(list_one) == 1:
        return list_one[0]

    s1 = sum(list_one)
    s2 = sum(list_two)

    return s1 - s2


if __name__ == '__main__':
    print(find_missing_element([4, 4, 2, 2], [2, 4, 2]))
