# anagram - we take two phrases and check if the both have the same set of letters.
from string import ascii_lowercase


def anagram(str_one: str, str_two: str) -> bool:
    """
    Check if two prases are anagrams.
    For simplicity the strings can contain only " " and english lowercase letters
    :param str_one: not empty string
    :param str_two: not empty string
    :return: True/False
    """
    assert isinstance(str_one, str), "str_one should be string"
    assert isinstance(str_two, str), "str_two should be string"
    len([i for i in str_one if i in ascii_lowercase + " "]) == len(str_one), """
    str_one should contain only ' ' and english lowercase letters"""
    len([i for i in str_two if i in ascii_lowercase + " "]) == len(str_two), """
    str_two should contain only ' ' and english lowercase letters"""

    str_one_dict = {}  # calculate number of different character in first string
    for i in str_one:
        if i != " ":  # ignore spaces
            if not str_one_dict.get(i):
                str_one_dict[i] = 1
            else:
                str_one_dict[i] += 1

    for i in str_two:
        if i != " ":
            if not str_one_dict.get(i):  # if character from str_two is not in str_one
                return False
            else:
                str_one_dict[i] -= 1
                if str_one_dict[i] < 0:  # if there are more characters of the same type
                    return False

    for i in str_one_dict.keys():
        if str_one_dict[i] != 0:
            return False
    else:
        return True


if __name__ == '__main__':
    print(anagram("a a a b c", " bca aa"))