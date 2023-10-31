class Node:
    def __init__(self, val: int | str) -> None:
        self.next: "Node" | None = None
        self.val: int | str = val

    def __str__(self) -> str:
        return f"N({self.val})"


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    def __str__(self) -> str:
        cur = self.head
        strings = []

        while cur is not None:
            strings.append(cur)
            cur = cur.next

        strings.append(str(cur))  # append None ad well

        strings = "->".join(map(str, strings))

        return f"LinkedList: {strings}"

    def append_head(self, val: int | str) -> None:
        node = Node(val)

        if (cur_head_node := self.head) is None:
            self.head = node
        else:
            self.head = node
            node.next = cur_head_node

    def append_tail(self, val: int | str) -> None:
        node = Node(val)

        cur = self.head

        if cur is None:
            self.head = node
        else:
            while cur.next is not None:
                cur = cur.next

            cur.next = node

    def reverse(self) -> None:
        prev = None
        cur = self.head

        while cur is not None:
            temp = cur.next  # next node, could be None
            cur.next = prev  # direct to prev Node or None
            prev = cur  # give prev value of cur
            cur = temp  # change cur to temp (cur.next for start)

        self.head = prev


if __name__ == '__main__':
    s1 = LinkedList()
    assert str(s1) == "LinkedList: None"
    s1.reverse()
    assert str(s1) == "LinkedList: None"

    [s1.append_head(i) for i in range(1, 6)]
    assert str(s1) == "LinkedList: N(5)->N(4)->N(3)->N(2)->N(1)->None"
    s1.reverse()
    assert str(s1) == "LinkedList: N(1)->N(2)->N(3)->N(4)->N(5)->None"
    s1.append_tail(6)
    assert str(s1) == "LinkedList: N(1)->N(2)->N(3)->N(4)->N(5)->N(6)->None"

    s2 = LinkedList()
    [s2.append_tail(i) for i in range(1, 6)]
    assert str(s2) == "LinkedList: N(1)->N(2)->N(3)->N(4)->N(5)->None"
