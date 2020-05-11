class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __repr__(self):
        return f"SingleLinkedNode(value={self.value})"


def make_reverse_list(x: LinkedListNode):
    assert type(x) == LinkedListNode
    CUR = x
    PREV = None
    while CUR:
        NEXT = CUR.next_node
        CUR.next_node = PREV
        PREV = CUR
        CUR = NEXT


if __name__ == '__main__':
    a = LinkedListNode("a")
    b = LinkedListNode("b")
    c = LinkedListNode("c")
    d = LinkedListNode("d")

    a.next_node = b
    b.next_node = c
    c.next_node = d

    make_reverse_list(a)

    print(d.next_node)
    print(c.next_node)
    print(b.next_node)
    print(a.next_node)
