class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __repr__(self):
        return f"SingleLinkedNode(value={self.value})"


def get_n_from_head_node_value(x: LinkedListNode, nth: int):
    assert isinstance(x, LinkedListNode)
    assert isinstance(nth, int), "Not Int"
    assert nth >= 0, "NOPE"
    cur = x
    for i in range(nth + 1):
        cur = cur.next_node
        if not cur:
            return None
    return cur.value


if __name__ == '__main__':
    a = LinkedListNode("a")

    a.next_node = None

    print(get_n_from_head_node_value(a, 0))
