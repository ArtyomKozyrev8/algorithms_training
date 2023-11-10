from .base_linked_list import BaseNode, BaseLinkedList


class Node(BaseNode):
    def __init__(self, val: int | str) -> None:
        self.next: "Node" | None = None
        self.val: int | str = val

    def __str__(self) -> str:
        return f"N({self.val})"


class LinkedList(BaseLinkedList):
    def __str__(self) -> str:
        cur = self.head
        strings = []

        while cur is not None:
            strings.append(cur)
            cur = cur.next

        strings.append(str(cur))  # append None ad well

        strings = "->".join(map(str, strings))

        return f"{self.class_name}: {strings}"

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
            raise IndexError(f"{self.class_name} instance is empty!")

        cur_next = cur.next

        self.head = cur_next

        return cur.val

    def remove_tail(self) -> int | str:
        cur = self.head

        if cur is None:
            raise IndexError(f"{self.class_name} instance is empty!")

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

    def remove_index(self, index: int) -> int | str:
        prev = None
        cur = self.head

        cur_index = 0
        while cur is not None:
            if cur_index == index:
                searched_item_val = cur.val
                if prev is not None:
                    prev.next = cur.next
                else:
                    self.head = cur.next

                return searched_item_val
            else:
                cur_index += 1
                prev = cur
                cur = cur.next

        raise IndexError(f"{self.class_name} instance does not contain index: {index}!")

    def remove_value(self, value: int | str) -> int | str:
        cur = self.head
        prev = None

        while cur is not None:
            if cur.val == value:
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next

                return cur.val
            else:
                prev = cur
                cur = cur.next

        raise ValueError(f"{self.class_name} instance does not contain value: {value}!")

    def insert_index(self, index: int, val: int | str) -> None:
        prev = None
        cur = self.head
        new_node = Node(val)

        if self.head is None:
            self.head = new_node  # if empty, add to head
            return None

        cur_index = 0
        while cur is not None:
            if cur_index == index:
                if prev is not None:
                    prev.next = new_node
                    new_node.next = cur
                else:
                    self.head = new_node
                    new_node.next = cur
                break

            cur_index += 1
            prev = cur
            cur = cur.next
        else:
            prev.next = new_node  # append to tail if index is out of range

        return None

    def reverse(self) -> None:
        prev = None
        cur = self.head

        while cur is not None:
            temp = cur.next  # next node, could be None
            cur.next = prev  # direct to prev Node or None
            prev = cur  # give prev value of cur
            cur = temp  # change cur to temp (cur.next for start)

        self.head = prev
