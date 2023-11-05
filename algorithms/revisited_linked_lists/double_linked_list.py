class Node:
    def __init__(self, val: int | str) -> None:
        self.next: "Node" | None = None
        self.prev: "Node" | None = None
        self.val: int | str = val

    def __str__(self) -> str:
        prev = self.prev
        if prev is not None:
            prev = prev.val

        next_ = self.next
        if next_ is not None:
            next_ = next_.val

        return f"N({self.val} [{prev}, {next_}])"


class DLL:
    def __init__(self) -> None:
        self.head: Node | None = None
        # self.cur_node is used for iterations (see __iter__ and __next__)
        self.class_name = self.__class__.__name__

    def __str__(self) -> str:
        cur = self.head
        strings = []

        while cur is not None:
            strings.append(cur)
            cur = cur.next

        strings.append(str(cur))  # append None ad well

        strings = "<->".join(map(str, strings))

        return f"{self.class_name}: {strings}"

    def __len__(self) -> int:
        len_ = 0
        cur = self.head

        while cur is not None:
            len_ += 1
            cur = cur.next

        return len_

    def append_head(self, val: int | str) -> None:
        node = Node(val)

        if self.head is None:
            self.head = node
            return

        cur = self.head

        self.head = node
        node.next = cur
        cur.prev = node


if __name__ == '__main__':
    s = DLL()
    print(s)
    s.append_head(1)
    print(s)

    s.append_head(2)
    print(s)

    s.append_head(3)
    print(s)

    s.append_head(4)
    print(s)
