def is_palindrome(x: str) -> str:
    """Checks if the string is palindrome"""
    if len(x) <= 1:
        return True
    if x[0] != x[-1]:
        return False
    return is_palindrome(x[1:len(x) - 1])


if __name__ == '__main__':
    print(is_palindrome("abcd"))
    print(is_palindrome(""))
    print(is_palindrome("a"))
    print(is_palindrome("aa"))
    print(is_palindrome("ab"))
    print(is_palindrome("aba"))
