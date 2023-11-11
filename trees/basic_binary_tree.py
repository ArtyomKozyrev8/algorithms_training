from typing import Optional


class BinaryTree:
    def __init__(self, val: int | str) -> None:
        self.val: int | str = val
        self.left_child: "BinaryTree" | None = None
        self.right_child: "BinaryTree" | None = None

    def __str__(self) -> str:
        return f"BT({self.val}, {self.left_child}, {self.right_child})"

    def insert_right(self, val: int | str) -> "BinaryTree":
        if self.right_child is None:
            self.right_child = BinaryTree(val)
        else:
            right_child_old = self.right_child
            self.right_child = BinaryTree(val)
            self.right_child.right_child = right_child_old

        return self

    def insert_left(self, val: int | str) -> "BinaryTree":
        if self.left_child is None:
            self.left_child = BinaryTree(val)
        else:
            left_child_old = self.left_child
            self.left_child = BinaryTree(val)
            self.left_child.left_child = left_child_old

        return self

    def get_value(self) -> int | str:
        return self.val

    def set_value(self, val: int | str) -> "BinaryTree":
        self.val = val

    def get_left_child(self) -> Optional["BinaryTree"]:
        return self.left_child

    def get_right_child(self) -> Optional["BinaryTree"]:
        return self.right_child
