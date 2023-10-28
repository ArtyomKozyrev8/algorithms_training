import string


def keep_only_letters(string_: str) -> str:
    new_str = []
    for letter in string_.lower():
        if letter in string.ascii_lowercase:
            new_str.append(letter)

    return "".join(new_str)


def is_palindrome(string_: str) -> bool:
    if len(string_) <= 1:
        return True
    elif string_[-1] != string_[0]:
        return False
    else:
        return is_palindrome(string_[1: len(string_) - 1])


if __name__ == '__main__':
    # structure of strings items: (string, is_palindrome answer)
    strings = (
        ("", True),
        ("x", True),
        ("radar", True),
        ("hello", False),
        ("hannah", True),
        ("madam i'm adam", True),
        ("Reviled did I live, said I, as evil I did deliver", True),
        ("Go hang a salami; I’m a lasagna hog.", True),
    )

    for item in strings:
        assert is_palindrome(keep_only_letters(item[0])) is item[1]
