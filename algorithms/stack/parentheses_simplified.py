from algorithms.stack.stack_implementation import Stack, StackEmpty


def check_parentheses(x: str) -> bool:
    """
    x - is a string which is composed of only '(' and ')' chars.
    Return true if parentheses have correct order when every opening parentheses
    have corresponding closing parentheses.
    The idea of the solution is that if we have '(' we put it into the Stack,
    if we see ')' we remove last element from stack. If we got no errors from
    Stack (in our case StackEmpty error) until end of string x and Stack is empty -
    we get True - the x is correct parentheses structure.
    :param x: the string
    :return: True or False
    """
    assert isinstance(x, str), "x should be string"
    storage = Stack()  # actually it is build on the top of list collection
    for i in x:
        if i == '(':
            storage.add(i)
        else:
            try:
                storage.pop()
            except StackEmpty:
                return False

    if storage.is_empty():
        return True
    return False


if __name__ == '__main__':
    strings = ["", "(", ")", "()", "()())", "(())(()())()()", "(())(())())()()", "((((())))())()()(())"]
    result = [check_parentheses(i) for i in strings]
    for i in zip(strings, result):
        print(i)


