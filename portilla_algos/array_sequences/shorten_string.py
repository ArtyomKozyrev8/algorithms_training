def compress_string(some_string: str) -> str:
    """
    some string is some kind of string in the following format "aaaAAAbbbCCCC"
    the funtcion should return compressed version of the string like "a3A3b3C4"
    :param some_string: some string
    :return: compressed string
    """
    assert isinstance(some_string, str), "some_string should be string"
    if not some_string:
        return some_string
    if len(some_string) == 1:
        return some_string[0] + "1"

    cur_letter = some_string[0]
    same_letters_in_row = 1
    compressed_str = ""
    for i in range(1, len(some_string)):
        if some_string[i] != cur_letter:
            compressed_str += cur_letter + str(same_letters_in_row)
            cur_letter = some_string[i]
            same_letters_in_row = 1
        else:
            same_letters_in_row += 1
    compressed_str += cur_letter + str(same_letters_in_row)
    return compressed_str


if __name__ == '__main__':
    print(compress_string("abc"))
    print(compress_string("a"))
    print(compress_string("aaaaab"))
    print(compress_string("aaaaabb"))
    print(compress_string(""))




