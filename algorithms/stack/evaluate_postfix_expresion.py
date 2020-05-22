from string import digits
from algorithms.stack.stack_implementation import Stack


def evaluate_postfix_expression(postfix_str: str) -> float:
    """
    Returns result of postfix expression string.
    :param postfix_str: postfix string is composed of digits, '.', '+', '-', '*', '/'
    :return: result of expression
    """
    storage = Stack()
    temp = ""
    not_operators = digits + "."
    for i in postfix_str:
        if i in not_operators:
            temp += i
        elif i == " ":
            # here we build number from the available digits
            if temp:
                temp = float(temp)
                storage.add(temp)
                temp = ""
        else:
            # if we find operator extract two elements (digits) from top of the Stack
            val_two = storage.pop()
            val_one = storage.pop()
            # and return result back to Stack
            storage.add(do_math(i, val_one, val_two))

    # the only element in Stack is the result of the postfix expression
    return storage.pop()


def do_math(operator_: str, val_one: float, val_two: float) -> float:
    """
    Perform the required operation and return it's result
    :param operator_: can be '*', '+', '/', '-'
    :param val_one: some float value
    :param val_two: some float value
    :return: some float value
    """
    if operator_ == '+':
        return val_one + val_two
    if operator_ == '-':
        return val_one - val_two
    if operator_ == "*":
        return val_one * val_two
    if operator_ == "/":
        return val_one / val_two
    raise ValueError(f"{operator_} is an incorrect operator")


if __name__ == '__main__':
    print(evaluate_postfix_expression("1.3 2 3 * + 5.5 +"))
    print(evaluate_postfix_expression("17 10 + 3 * 9 /"))
    print(evaluate_postfix_expression("10 3 5 * 16 4 - / +"))
