from abc import ABC
from collections.abc import Sequence


class BaseNode(ABC):
    pass


class BaseLinkedList(Sequence):
    def __init__(self) -> None:
        self.head: BaseNode | None = None
        # self.cur_node is used for iterations (see __iter__ and __next__)
        self.cur_node: BaseNode | None = self.head
        self.class_name = self.__class__.__name__

    def __len__(self) -> int:
        len_ = 0
        cur = self.head

        while cur is not None:
            len_ += 1
            cur = cur.next

        return len_

    def __contains__(self, item: int | str) -> bool:
        cur = self.head
        contains = False

        while cur is not None:
            if cur.val == item:
                contains = True
                break

            cur = cur.next

        return contains

    def __iter__(self) -> "LinkedList":
        self.cur_node = self.head
        return self

    def __next__(self) -> int | str:
        while self.cur_node is not None:
            cur_val = self.cur_node.val
            self.cur_node = self.cur_node.next
            return cur_val

        raise StopIteration

    def __getitem__(self, index: int) -> int | str:
        cur_index = 0
        cur = self.head

        while cur is not None:
            if cur_index == index:
                break

            cur = cur.next
            cur_index += 1
        else:
            raise IndexError(f"{self.class_name} instance does not contain index: {index}")

        return cur.val
