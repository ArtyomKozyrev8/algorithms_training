# not finished!!!


def string_permutations_combos(s: str) -> list:
    """
    Returns number of  possible string letters combinations
    :param s: some string
    :return: list of possible string letter combinations
    """
    assert isinstance(s, str), "s should be string"

    if len(s) <= 1:
        return s

    combos = []
    for i, letter in enumerate(s):
        combos.append(letter + string_permutations_combos(s[:i] + s[i+1:]))
    return combos


if __name__ == '__main__':
    print(string_permutations_combos("ab"))
