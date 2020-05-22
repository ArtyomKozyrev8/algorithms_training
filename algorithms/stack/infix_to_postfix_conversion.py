from algorithms.stack.stack_implementation import Stack


def convert_from_infix_to_postfix(infix_str: str) -> str:
    """
    Converts string from infix type to prefix type string.
    The idea is that if we see letter we just put it in new_string.
    All operators go to Stack, operators with higher priority remove operators which were earlier from the Stack
    till the Stack if empty or till it founds '('
    if we get ')' we push all operators till '(' ('(' is also removed from Stack but do not go to new_string)
    from Stack and add them to new_string
    :param infix_str: is composed of operators '+': 3, '-': 3, '*': 2, '/': 2, '(': 1, ')': 1 and letters
    """
    # order_levels - priority levels of operators
    order_levels = {'+': 3, '-': 3, '*': 2, '/': 2, '(': 1, ')': 1}

    operators_storage = Stack()  # temporary storage for for operators
    new_str = []  # base for prefix type string

    for i in infix_str:
        if i == " ":
            continue
        if i not in list(order_levels.keys()):  # just letter
            new_str.append(i)
        else:
            if i == '(':
                operators_storage.add(i)
            elif i == ')':
                while True:
                    temp = operators_storage.pop()
                    if temp == '(':
                        break
                    new_str.append(temp)
            else:
                if not operators_storage.is_empty():
                    if order_levels[operators_storage.peek()] <= order_levels[i]:
                        while not operators_storage.is_empty():
                            if operators_storage.peek() == '(':
                                break
                            temp = operators_storage.pop()
                            new_str.append(temp)
                        operators_storage.add(i)
                    else:
                        operators_storage.add(i)
                else:
                    operators_storage.add(i)
    # when we checked all element of old string, we should remove all left operators from Stack
    while not operators_storage.is_empty():
        temp = operators_storage.pop()
        new_str.append(temp)

    return " ".join(new_str)


if __name__ == '__main__':
    tests = ["A + B * C + D", "( A + B ) * ( C + D )", "A * B + C * D", "A + B + C + D",
             "( A + B ) * C - ( D - E ) * ( F + G )", "( ( A + B ) * (C + D) ) + E"]
    results = {i: convert_from_infix_to_postfix(i) for i in tests}
    for k, v in results.items():
        print(f"{k} : {v}")
