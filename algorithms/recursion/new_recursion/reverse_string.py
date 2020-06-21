def reverse_str(x: str) -> str:
    """Take string and returns the revert form of the string"""
    if len(x) <= 1:
        return x
    return x[-1] + reverse_str(x[:len(x) - 1])


if __name__ == '__main__':
    print(reverse_str("abcd"))
    print(reverse_str(""))
    print(reverse_str("a"))
