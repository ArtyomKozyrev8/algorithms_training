class SingleLinkedNode:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __repr__(self):
        return f"SingleLinkedNode(value={self.value})"


if __name__ == '__main__':
    a = SingleLinkedNode("a")
    b = SingleLinkedNode("b")
    c = SingleLinkedNode("c")
    d = SingleLinkedNode("d")
    e = SingleLinkedNode("e")

    a.next_node = b
    b.next_node = c
    c.next_node = d
    d.next_node = e

    print(b.next_node)
