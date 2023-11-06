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

        return f"N({self.val}[{prev}, {next_}])"


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

        if not strings:
            strings.append(str(cur))  # append None ad well

        strings = "=".join(map(str, strings))

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

        return

    def pop_head(self) -> int | str:
        if self.head is None:
            raise IndexError(f"{self.class_name} instance is empty!")

        cur = self.head
        next_cur = cur.next

        if next_cur is None:
            self.head = None
        else:
            self.head = next_cur
            next_cur.prev = None

        return cur.val

    def append_tail(self, val: int | str) -> None:
        node = Node(val)

        if self.head is None:
            self.head = node
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next

        cur.next = node
        node.prev = cur

        return

    def pop_tail(self) -> int | str:
        if self.head is None:
            raise IndexError(f"{self.class_name} instance is empty!")

        cur = self.head

        while True:
            if cur.next is None:
                break
            else:
                cur = cur.next

        prev = cur.prev
        if prev is None:
            self.head = None
        else:
            prev.next = None

        return cur.val

    def reverse(self) -> None:
        if self.head is None:
            return

        cur = self.head
        while True:
            cur_next = cur.next
            if cur_next is None:
                old_prev = cur.prev
                self.head = cur
                cur.prev = None
                cur.next = old_prev
                break
            else:
                old_prev = cur.prev
                cur.next = old_prev
                cur.prev = cur_next
                cur = cur_next

        return
