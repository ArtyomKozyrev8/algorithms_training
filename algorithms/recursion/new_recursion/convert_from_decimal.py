def convert_from_dec(number: int, base: int) -> str:
    """
    Coverts number from decimal to bin, oct or hex system
    :param number: some positive decimal number
    :param base: 2, 8, 16
    :return: string representation of number in the desired format
    """
    base_digits = "0123456789ABCDEF"
    if number < base:
        return base_digits[number]

    return convert_from_dec(number // base, base) + base_digits[number % base]


if __name__ == '__main__':
    for i in range(0, 20):
        print(f"{i} : {convert_from_dec(i, 2)}")
    for i in range(0, 20):
        print(f"{i} : {convert_from_dec(i, 16)}")
    for i in range(224, 256):
        print(f"{i} : {convert_from_dec(i, 16)}")
    print(f"{255} : {convert_from_dec(i, 8)}")
