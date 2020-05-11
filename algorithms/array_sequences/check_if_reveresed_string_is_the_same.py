def check_if_reversed_string_is_the_same_pythonic(x: str) -> bool:
    """
    Checks if the reversed string is the same as initial one.
    :param x: some string
    :return: True/False
    """
    assert isinstance(x, str), "x should be string"
    assert len(x) > 0, "x can't be empty string"
    if len(x) == 1:
        return True
    return x == x[::-1]


def check_if_reversed_string_is_the_same(x: str) -> bool:
    """
    Checks if the reversed string is the same as initial one.
    :param x: some string
    :return: True/False
    """
    assert isinstance(x, str), "x should be string"
    assert len(x) > 0, "x can't be empty string"
    if len(x) == 1:
        return True
    reversed_string = ""
    x_len = len(x) - 1
    while x_len >= 0:
        reversed_string += x[x_len]
        x_len -= 1
    if reversed_string == x:
        return True
    return False


if __name__ == '__main__':
    print(check_if_reversed_string_is_the_same_pythonic("a"))
    print(check_if_reversed_string_is_the_same("ababa"))
