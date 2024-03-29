from .singly_linked_list import Node, LinkedList


def _more_or_equal(a: int | str, b: int | str, reversed_: bool = True) -> bool:
    if not reversed_:
        return a >= b
    else:
        return a <= b


class OrderedLinkedList(LinkedList):
    def __init__(self, reversed_: bool = False):
        super().__init__()
        self.reversed = reversed_

    def __str__(self) -> str:
        cur = self.head
        strings = []

        while cur is not None:
            strings.append(cur)
            cur = cur.next

        strings.append(str(cur))  # append None ad well

        strings = "->".join(map(str, strings))

        return f"{self.class_name}: {strings}"

    def __contains__(self, item: int | str) -> bool:
        cur = self.head

        while cur is not None:
            if cur.val == item:
                return True
            elif _more_or_equal(cur.val, item, self.reversed):
                return False
            else:
                cur = cur.next

        return False

    def append(self, val: int | str) -> None:
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        cur = self.head
        prev = None

        while cur is not None:
            if cur.next is None or _more_or_equal(cur.val, new_node.val, self.reversed):
                if _more_or_equal(cur.val, new_node.val, self.reversed):
                    if prev is None:
                        self.head = new_node
                        new_node.next = cur
                    else:
                        prev.next = new_node
                        new_node.next = cur
                else:
                    next_ = cur.next
                    cur.next = new_node
                    new_node.next = next_
                break
            else:
                prev = cur
                cur = cur.next

        return

    def append_head(self, val: int | str) -> None:
        return self.append(val)

    def append_tail(self, val: int | str) -> None:
        return self.append(val)

    def reverse(self) -> None:
        raise AttributeError(f"{self.class_name} does not implement reverse()!")

    def insert_index(self, index: int, val: int | str) -> None:
        raise AttributeError(f"{self.class_name} does not implement insert_index()!")
