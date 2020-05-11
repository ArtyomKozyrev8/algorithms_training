class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next_node = None


def check_if_circle(x: LinkedListNode):
    assert type(x) == LinkedListNode
    slow = x
    fast = x

    while fast.next_node:
        fast = fast.next_node
        if not fast.next_node:
            return False
        fast = fast.next_node
        slow = slow.next_node

        if slow is fast:
            return True

    return False


if __name__ == '__main__':
    a = LinkedListNode("a")
    b = LinkedListNode("b")
    c = LinkedListNode("c")
    d = LinkedListNode("d")

    a.next_node = b
    b.next_node = c
    c.next_node = d
    d.next_node = None

    print(check_if_circle(a))
