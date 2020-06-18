from algorithms.linked_list.new_linked_list.node import LListNode


class UnorderedListBaseError(Exception):
    """UnorderedList Base Error Class"""
    pass


class UnorderedListEmptyError(UnorderedListBaseError):
    """Is raised when we try to remove element from empty UnorderedList"""


class UnorderedList:
    """Unordered List implementation based on Liked List"""
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head:
            return False
        return True

    def __len__(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.get_next()
        return count

    def __repr__(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(str(curr.get_value()))
            curr = curr.get_next()
        return f"UnorderedList({', '.join(elements)})"

    def append(self, value):
        temp = LListNode(value)
        temp.set_next(self.head)
        self.head = temp

    def pop(self):
        if not self.head:
            raise UnorderedListEmptyError("Can't pop from empty UnorderedList")
        temp = self.head.get_value()
        next_node = self.head.get_next()
        self.head = next_node
        return temp


if __name__ == '__main__':
    x = UnorderedList()
    for i in range(0, 6):
        x.append(i)
        print(f"{x} Len {len(x)} Empty {x.is_empty()}")
    for i in range(0, 6):
        t = x.pop()
        print(f"{x} Len {len(x)} Empty {x.is_empty()} Poped {t}")

