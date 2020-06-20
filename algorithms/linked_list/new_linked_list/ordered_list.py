from algorithms.linked_list.new_linked_list.node import LListNode
from algorithms.linked_list.new_linked_list.unordered_list import UnorderedList


class OrderedList(UnorderedList):
    def __repr__(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(str(curr.get_value()))
            curr = curr.get_next()
        return f"OrderedList({', '.join(elements)})"

    def append_to_head(self, value):
        temp = LListNode(value)
        if not self.head:
            self.head = temp
            return

        prev_node = None
        curr = self.head
        while curr:
            if curr.get_value() >= value:
                break
            prev_node = curr
            curr = curr.get_next()
        if prev_node:
            temp.set_next(curr)
            prev_node.set_next(temp)
        else:
            temp.set_next(curr)
            self.head = temp


if __name__ == '__main__':
    x = OrderedList()
    for i in [5, 2, 8, 7, 9, 12]:
        x.append_to_head(i)
        print(x)
