class Node:
    def __init__(self, val: int | str) -> None:
        self.next: "Node" | None = None
        self.val: int | str = val

    def __str__(self) -> str:
        return f"N({self.val})"


class BaseLinkedListError(Exception):
    pass


class EmptyLinkedListError(BaseLinkedListError):
    pass


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

    def __len__(self) -> int:
        len_ = 0
        cur = self.head

        while cur is not None:
            len_ += 1
            cur = cur.next

        return len_

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

    def remove_head(self) -> int | str:
        cur = self.head

        if cur is None:
            raise EmptyLinkedListError("LinkedList is empty!")

        cur_next = cur.next

        self.head = cur_next

        return cur.val

    def remove_tail(self) -> int | str:
        cur = self.head

        if cur is None:
            raise EmptyLinkedListError("LinkedList is empty!")

        prev = cur
        cur = cur.next

        if cur is None:
            self.head = None
            return prev.val

        while cur.next is not None:
            prev = cur
            cur = cur.next

        prev.next = None

        return cur.val

    def __getitem__(self, index: int) -> int | str:
        cur_index = 0
        cur = self.head

        while cur is not None:
            if cur_index == index:
                break

            cur = cur.next
            cur_index += 1
        else:
            raise IndexError(f"No element with index: {index}")

        return cur.val

    def reverse(self) -> None:
        prev = None
        cur = self.head

        while cur is not None:
            temp = cur.next  # next node, could be None
            cur.next = prev  # direct to prev Node or None
            prev = cur  # give prev value of cur
            cur = temp  # change cur to temp (cur.next for start)

        self.head = prev
