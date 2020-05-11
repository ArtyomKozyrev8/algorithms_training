class DoublyLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

    def __repr__(self):
        return f"DoublyLinkedListNode(value={self.value})"


if __name__ == '__main__':
    a = DoublyLinkedListNode("a")
    b = DoublyLinkedListNode("b")
    c = DoublyLinkedListNode("c")
    d = DoublyLinkedListNode("d")

    a.next_node = b
    b.prev_node = a
    b.next_node = c
    c.prev_node = b
    c.next_node = d
    d.prev_node = c

    print(c.prev_node, c.next_node)
