def string_permutations_combos(string_: str) -> list[str]:
    combos = []

    if len(string_) == 1:
        return [string_]

    for i, s in enumerate(string_):
        for str_ in string_permutations_combos(string_[:i] + string_[i + 1:]):
            combos.append(s + str_)

    return sorted(combos)


if __name__ == '__main__':
    inputs = (
        ("", []),
        ("a", ["a"]),
        ("ab", sorted(["ab", "ba"])),
        ("abc", sorted(["abc", "acb", "bac", "bca", "cab", "cba"])),
    )

    for item in inputs:
        assert string_permutations_combos(item[0]) == item[1]
