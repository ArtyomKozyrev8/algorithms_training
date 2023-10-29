def calc_string_permutations_number(string_: str) -> int:
    """
    Returns number of  possible string letters combinations
    :param string_: some string
    :return: number of possible string letter combinations
    """
    cache = dict()

    def calc_string_permutations_number_inner(s: str) -> int:
        permutations_number = 0

        if len(s) == 1:
            return 1

        for _ in s:
            # letter does not matter, we just count number
            # so, we do not use letter, we just use s[1:]
            if len(s[1:]) in cache:
                permutations_number += cache[len(s[1:])]
            else:
                val = calc_string_permutations_number_inner(s[1:])
                cache[len(s[1:])] = val
                permutations_number += val

        return permutations_number

    return calc_string_permutations_number_inner(string_)


if __name__ == '__main__':
    inputs = (
        ("", 0),
        ("a", 1),
        ("ab", 2),
        ("abc", 6),
        ("abcd", 24),
        ("abcde", 120),
        ("abcdef", 720),
        ("abcdefg", 5040),
        ("abcdefg", 5040),
        ("abcdefgh", 40320),
        ("abcdefghi", 362_880),
        ("abcdefghij", 3_628_800),
    )

    for item in inputs:
        assert calc_string_permutations_number(item[0]) == item[1]
