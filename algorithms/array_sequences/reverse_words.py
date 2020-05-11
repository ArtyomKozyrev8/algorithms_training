def reverse_words(some_string: str) -> str:
    """
    some_string - is some sentence which is composed of only white spaces and english letters
    returns reversed sentence
    :param some_string: some sentence
    :return: reversed sentence
    """
    assert isinstance(some_string, str), "some_string shoudld be string"
    if not len(some_string):
        return ""
    some_string = [i for i in some_string.split() if i]
    return " ".join(reversed(some_string))


if __name__ == '__main__':
    print(reverse_words("    hello    my dear   friend  "))
    print(reverse_words("  "))
    print(reverse_words("a"))
