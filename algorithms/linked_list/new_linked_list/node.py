class LListNode:
    """Is used as a building block for LinkedList Classes"""
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def set_next(self, node):
        self.next_node = node

    def get_next(self):
        return self.next_node

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def __repr__(self):
        return f"LListNode({self.value})"


if __name__ == '__main__':
    x1 = LListNode(1)
    x2 = LListNode(2)
    x1.set_next(x2)
    print(x1)
    print(x2)
    print(x1.get_next())
    print(x2.get_next())
    print(x2.get_value())
