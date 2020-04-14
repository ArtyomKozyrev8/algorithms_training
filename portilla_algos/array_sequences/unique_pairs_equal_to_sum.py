def find_unique_pairs_equal_to_sum(list_ints: list, sum_: int) -> list:
    """
    Find all unique pairs of integers in list_ints which sum is eqaul to sum_
    :param list_ints: list of some integer values
    :param sum_: integer, the expected sum of two list_ints members
    :return: list of tuples
    """
    assert isinstance(sum_, int), "sum_ should be integer"
    assert sum_ >= 0, "sum_ should be >= 0"
    assert isinstance(list_ints, list), "list_ints should be list"
    assert len(list_ints) >= 2, "length of list_ints should be >= 2"
    assert len([i for i in list_ints if isinstance(i, int)]) == len(list_ints), "list_ints should be list of integers"
    output = []
    for i in range(len(list_ints) - 1):
        for j in range(i + 1, len(list_ints)):
            if list_ints[i] + list_ints[j] == sum_:
                if list_ints[i] > list_ints[j]:
                    if not (list_ints[j], list_ints[i], ) in output:
                        output.append((list_ints[j], list_ints[i], ))
                else:
                    if not (list_ints[i], list_ints[j], ) in output:
                        output.append((list_ints[i], list_ints[j],))
    return output


if __name__ == '__main__':
    print(find_unique_pairs_equal_to_sum([1, 4, 2, 6, 2, 3, 5, 1, 0], 6))
    print(find_unique_pairs_equal_to_sum([4, 2], 6))