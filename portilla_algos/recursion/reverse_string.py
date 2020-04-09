def reverse_string(str_: str) -> str:
    """
    Takes string and returns it's reversed version
    :param str_: some string
    :param empty_string: should be empty string
    :return: reversed string
    """
    assert isinstance(str_, str), "Should be string"
    if len(str_) < 1:
        return str_

    return str_[-1] + reverse_string(str_[:len(str_) - 1])


if __name__ == '__main__':
    print(reverse_string("abcdef"))
