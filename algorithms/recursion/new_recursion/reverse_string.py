def reverse_str_recursive(string_: str) -> str:
    new_str = ""

    if not string_:
        new_str = ""
    else:
        new_str += string_[-1] + reverse_str_recursive(string_[0: len(string_) - 1])

    return new_str


if __name__ == '__main__':
    for str_ in ("abcd", "", "a", "ab", "aaa"):
        assert reverse_str_recursive(str_) == str_[::-1]
