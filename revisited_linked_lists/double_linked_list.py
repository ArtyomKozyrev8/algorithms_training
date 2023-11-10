from .base_linked_list import BaseNode, BaseLinkedList


class Node(BaseNode):
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


class DLL(BaseLinkedList):
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

    def remove_index(self, index: int) -> int | str:
        cur = self.head

        cur_index = 0
        while cur is not None:
            if cur_index == index:
                prev = cur.prev
                next_ = cur.next
                if prev is None:
                    self.head = next_
                    if next_ is not None:
                        next_.prev = prev
                else:
                    prev.next = next_
                    if next_ is not None:
                        next_.prev = prev

                return cur.val
            else:
                cur_index += 1
                cur = cur.next

        raise IndexError(f"{self.class_name} instance does not contain index: {index}!")

    def remove_value(self, value: int | str) -> int | str:
        cur = self.head

        while cur is not None:
            if cur.val == value:
                cur_next = cur.next
                cur_prev = cur.prev
                if cur_prev is None:
                    self.head = cur_next
                    if cur_next is not None:
                        cur_next.prev = None
                else:
                    cur_prev.next = cur_next
                    if cur_next is not None:
                        cur_next.prev = cur_prev

                return cur.val
            else:
                cur = cur.next

        raise ValueError(f"{self.class_name} instance does not contain value: {value}!")

    def insert_index(self, index: int, val: int | str) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return

        cur_index = 0
        cur = self.head

        while True:
            if index == cur_index:
                prev = cur.prev
                if prev is None:
                    self.head = new_node
                    new_node.next = cur
                    cur.prev = new_node
                else:
                    new_node.prev = prev
                    prev.next = new_node
                    new_node.next = cur
                    cur.prev = new_node

                return
            else:
                cur_next = cur.next
                if cur_next is None:
                    break
                cur_index += 1
                cur = cur_next

        cur.next = new_node
        new_node.prev = cur
        return

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
