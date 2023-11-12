import operator

from .basic_binary_tree import BinaryTree


def build_parse_tree(expression: str) -> BinaryTree:
    """
    param: expression must be separated by '(' and ')' .
    Example: a. '((7+3)*(5-2))'  b. '(3*(4+5))' .

    You can use only digit 0,1,2,3,4,5,6,7,8,9.
    You can use 99, 14, -5, 100, etc.
    """
    expression = [i for i in expression if i != " "]
    stack = []  # use list as a stack structure
    # stack is used to store parent nodes
    cur = BinaryTree("")  # start with empty binary tree
    stack.append(cur)  # append cur empty tree to stack

    for part in expression:
        if part == "(":
            # this is a start of new expression
            # each expression is a new binary tree
            cur.insert_left("")  # we read from left to right
            stack.append(cur)  # memorise parent
            cur = cur.get_left_child()  # go to new node
        elif part.isdigit():
            cur.set_value(part)  # just set value
            cur = stack.pop()  # go to parent node
        elif part in ("+", "-", "/", "*"):
            cur.set_value(part)  # set root value ad a sign
            cur.insert_right("")  # create new node as we expect right side of expression
            stack.append(cur)  # memorise root
            cur = cur.get_right_child()  # go to the new node
        elif part in ")":
            cur = stack.pop()  # go to upper node
        else:
            raise ValueError(f"Unexpected value of part: {part}")

    if len(stack) > 0:
        raise ValueError(f"We do something wrong! Stack should be empty!")

    return cur


def evaluate_parse_tree(tree: BinaryTree) -> int:
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    if tree.left_child is None:
        return int(tree.val)

    if tree.right_child is None:
        return int(tree.val)

    result = ops[tree.val](evaluate_parse_tree(tree.get_left_child()), evaluate_parse_tree(tree.get_right_child()))

    return result
