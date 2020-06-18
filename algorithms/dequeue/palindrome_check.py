from algorithms.dequeue.deque_impl import MyDequeEmptyError, MyDeque

def check_if_word_is_palindrome(word: str) -> bool:
    """
    Checks if the word is palindrome.
    Palindrome is the word which is same if we read it from rear to front end.
    :param word: the word we would like to check
    :return: True | False
    """
    assert isinstance(word, str), "word should be string"
    if not len(word):
        return False
    x = MyDeque()
    for w in word:
        x.add_to_rear_end(w)

    while(len(x) > 1):
        rear = x.remove_from_rear_enf()
        front = x.remove_from_front_end()
        if rear != front:
            return False
    return True

if __name__ == '__main__':
    print(check_if_word_is_palindrome(""))
    print(check_if_word_is_palindrome("a"))
    print(check_if_word_is_palindrome("ab"))
    print(check_if_word_is_palindrome("cac"))
    print(check_if_word_is_palindrome("madam"))
    print(check_if_word_is_palindrome("pers"))
    print(check_if_word_is_palindrome("dddd"))
