class LLNode:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __repr__(self):
        return f"LLNode{self.value}"


def reverse_ll(x: LLNode):
    P = None
    cur = x

    while cur.next_node:
        N = cur.next_node  # fix next node
        cur.next_node = P  # direct current to previous node
        P = cur  # change previous
        # print(f"PREV: {P}") # to debug
        cur = N  # give current the fix (reserved value)
        # print(f"CUR: {cur}") # to debug
        # print(f"CUR_NEXT: {cur.next_node}") # to debug

    cur.next_node = P

    return cur


if __name__ == '__main__':
    # test data
    x1 = LLNode(1)
    x2 = LLNode(2)
    x3 = LLNode(3)
    x4 = LLNode(4)
    x5 = LLNode(5)
    x6 = LLNode(6)
    # connect in singly linked list
    x1.next_node = x2
    x2.next_node = x3
    x3.next_node = x4
    x4.next_node = x5
    x5.next_node = x6

    z1 = LLNode(0)  # another test data

    y = reverse_ll(z1)  # reverse singly linked list

    while y:
        print(y)
        y = y.next_node
    print(y)
