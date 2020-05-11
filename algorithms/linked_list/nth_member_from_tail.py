class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __repr__(self):
        return f"SingleLinkedNode(value={self.value})"


def nth_member_from_the_end(x: LinkedListNode, nth: int):
    assert isinstance(x, LinkedListNode)
    assert isinstance(nth, int), "Not Int"
    assert nth >= 0, "NOPE"
    cur = x
    n_member_from_tail = x
    for i in range(0, nth - 1):
        cur = cur.next_node
        if not cur:
            raise LookupError("Not enough members")
    print(cur.value)
    while cur:
        cur = cur.next_node
        if cur:
            n_member_from_tail = n_member_from_tail.next_node

    return n_member_from_tail.value


if __name__ == '__main__':
    a = LinkedListNode("a")
    b = LinkedListNode("b")
    c = LinkedListNode("c")
    d = LinkedListNode("d")
    e = LinkedListNode("e")

    a.next_node = b
    b.next_node = c
    c.next_node = d
    d.next_node = e

    print(nth_member_from_the_end(a, 2))
