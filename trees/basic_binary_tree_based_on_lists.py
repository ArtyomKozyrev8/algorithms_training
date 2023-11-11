from typing import NewType

BinaryTree = NewType("BinaryTree", list[int, list["BinaryTree"], list["BinaryTree"]])


def make_binary_tree(value: int) -> BinaryTree:
    return [value, [], []]


def insert_right(root: BinaryTree, value: int) -> BinaryTree:
    if not root[2]:
        # if no right child, we just insert new tree node instead of empty list (old right child)
        root[2] = [
            value,
            [],
            [],
        ]
    else:
        # if we have some right child we insert it as a right child of a new one
        old_node = root[2]  # remember current right child

        root[2] = [
            value,
            [],
            old_node,  # use old right child as a right child of the new right child
        ]

    return root


def insert_left(root: BinaryTree, value: int) -> BinaryTree:
    if not root[1]:
        root[1] = [
            value,
            [],
            [],
        ]
    else:
        old_node = root[1]

        root[1] = [
            value,
            old_node,
            [],
        ]

    return root


def get_root_value(root: BinaryTree) -> int:
    return root[0]


def set_root_val(root: BinaryTree, value: int) -> BinaryTree:
    root[0] = value

    return root


def get_left_child(root: BinaryTree) -> BinaryTree | list:
    return root[1]


def get_right_child(root: BinaryTree) -> BinaryTree | list:
    return root[2]
