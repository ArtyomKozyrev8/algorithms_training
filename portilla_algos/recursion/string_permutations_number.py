def string_permutations_number(s: str) -> int:
    """
    Returns number of  possible string letters combinations
    :param s: some string
    :return: number of possible string letter combinations
    """
    assert isinstance(s, str), "s should be string"

    if len(s) <= 1:
        return 1

    perm_number = 0  # should be made zero every step
    for i, letter in enumerate(s):
        perm_number = perm_number + string_permutations_number(s[:i] + s[i+1:])
    return perm_number


if __name__ == '__main__':
    print(string_permutations_number("abcde"))

