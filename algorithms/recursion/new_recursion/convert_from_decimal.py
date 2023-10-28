from enum import Enum


class NumericSystemEnum(Enum):
    binary = 2
    oct = 8
    decimal = 10


def convert_from_decimal_to_another(number: int, num_system: NumericSystemEnum) -> int:
    base = num_system.value
    result_string = ""
    if number < base:
        result_string = str(number) + result_string
    else:
        result_string = convert_from_decimal_to_another(number // base, num_system) + str(number % base)

    return result_string


if __name__ == '__main__':
    inputs_ = (
        (11, NumericSystemEnum.binary, "1011"),
        (0, NumericSystemEnum.binary, "0"),
        (8, NumericSystemEnum.binary, "1000"),
        (2, NumericSystemEnum.binary, "10"),
        (1, NumericSystemEnum.binary, "1"),
        (13, NumericSystemEnum.decimal, "13"),
        (0, NumericSystemEnum.decimal, "0"),
        (8, NumericSystemEnum.decimal, "8"),
        (2, NumericSystemEnum.decimal, "2"),
        (1, NumericSystemEnum.decimal, "1"),
        (28, NumericSystemEnum.oct, "34"),
        (344, NumericSystemEnum.oct, "530"),
        (0, NumericSystemEnum.oct, "0"),
        (8, NumericSystemEnum.oct, "10"),
        (2, NumericSystemEnum.oct, "2"),
        (1, NumericSystemEnum.oct, "1"),
    )

    for item in inputs_:
        assert convert_from_decimal_to_another(item[0], item[1]) == item[2]
