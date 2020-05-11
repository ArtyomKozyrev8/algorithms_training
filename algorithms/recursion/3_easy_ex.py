from string import digits


def cumulative_sum(n: int) -> int:
    """
    Returns cumulative sum of al integer from zero to n
    :param n: some integer number, which is greater or equal to zero
    :return: cumulative sum of al integer from zero to n
    """
    assert isinstance(n, int), "n should be integer"
    assert n >= 0, "n should be >= 0"
    if n == 0:
        return 0
    return n + cumulative_sum(n-1)


def split_string_sum_numbers(str_: str) -> int:
    """
    Split string which is composed of integer numbers from 0 to 9, them sum all the number
    :param str_: string which is composed of integers >= 0 and <= 9
    :return: sum of integers
    """
    assert isinstance(str_, str), "str_ should be string"
    assert len(str_) > 0, "str+ should be not empty integer"
    assert len([i for i in str_ if i in digits]) == len(str_), "str_ should be composed of digits"
    if len(str_) == 1:
        return int(str_)
    return int(str_[0]) + split_string_sum_numbers(str_[1:])


def check_if_string_is_splittable(str_: str, options_: list, output: list) -> list:
    """
    Check is string can be splitted in the list of words which are provided in options_.
    Example: str_ = thetherabbit, options_ = [the, rabbit]. The Result will be ['the', 'the', 'rabbit']
    IMPORTANT NOTE: pay attention that if str_ = "rabbit" and options_ = ["r", "rabbit" you will get
    ["NO LUCK"], on the other hand if options_ = ["rabbit", "r"] you will get ["rabbit].
    HEREBY ORDER OF OPTIONS IS IMPORTANT FOR THE SOLUTION.
    Better solution can be achieved if we change order of options in case of failed operation.
    :param str_: some string we gonna try to split
    :param options_: list of strings
    :param output: should always be an empty list
    :return: splited str_
    """
    assert isinstance(str_, str), "str_ should be string"
    assert len(options_) > 0, "options should be not empty list"
    assert isinstance(options_, list), "options_ should be list"
    assert len([i for i in options_ if isinstance(i, str)]) == len(options_), "options_ should be list of strings"
    if len(str_) == 0:
        return output

    for i in options_:
        if str_.startswith(i):
            output.append(str_[0: len(i)])
            return check_if_string_is_splittable(str_[len(i):], options_, output)
    else:
        return ["NO LUCK"]


if __name__ == '__main__':
    print(cumulative_sum(5))
    print(split_string_sum_numbers("1234"))
    print(check_if_string_is_splittable("therabbit", ["the", "rabbit"], []))