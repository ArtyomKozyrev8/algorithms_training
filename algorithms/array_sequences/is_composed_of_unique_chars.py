def is_composed_of_unique_chars(some_string) -> bool:
    """
    Checks if some_string is composed of only unique characters, if yes - return True, otherwise - False
    :param some_string: some random string
    :return: True/False
    """
    assert isinstance(some_string, str), "some_string should be string"
    if len(some_string) <= 1:
        return True

    count_unique = dict()
    for i in some_string:
        if not count_unique.get(i):
            count_unique[i] = 1
        else:
            return False
    return True


if __name__ == '__main__':
    print(is_composed_of_unique_chars(""))
    print(is_composed_of_unique_chars("A"))
    print(is_composed_of_unique_chars("aahde"))
    print(is_composed_of_unique_chars("ahdeff"))
    print(is_composed_of_unique_chars("abcder"))
