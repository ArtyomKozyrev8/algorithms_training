from algorithms.stack.stack_implementation import Stack, StackEmpty


def check_parentheses(x: str) -> bool:
    """
    x - is a string which is composed of only '(', '{', '[ and ')', '}', ']' chars.
    Return true if parentheses have correct order when every opening parentheses
    have corresponding closing parentheses.
    The idea of the solution is that if we have '(', '{', '[we put it into the Stack,
    if we see ')', '}', ']' we remove last element from stack if it is the correct bracket.
    If we got no errors from Stack (in our case StackEmpty error)
    until end of string x and Stack is empty - we get True - the x is correct parentheses structure.
    :param x: the string
    :return: True or False
    """
    assert isinstance(x, str), "x should be string"
    s = Stack()
    for i in x:
        if i in ["(", "{", "["]:
            s.add(i)
        else:
            try:
                t = s.pop()
                if t + i in ["()", "{}", "[]"]:
                    pass
                else:
                    return False
            except StackEmpty:
                return False
    if s.is_empty():
        return True
    return False


if __name__ == '__main__':
    strings = [
        "", "(", ")", "()", "()())", "(())(()())()()", "(())(())())()()", "((((())))())()()(())",
        "[]{}", "[({})()[]{()}]", "[({)}()][]()", "{()}[](){}{", "[{()}]{()}[]{([[[()]]])}"
    ]
    result = [check_parentheses(i) for i in strings]
    for i in zip(strings, result):
        print(i)
