class BinaryTree:
    def __init__(self, root_value):
        self.root_value = root_value
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return f"BinaryTree({self.root_value}, {self.left_child}, {self.right_child})"

    def set_root_value(self, value):
        self.root_value = value

    def get_root_value(self):
        return self.root_value

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def insert_left_child(self, left_child_value):
        if not self.left_child:
            self.left_child = BinaryTree(left_child_value)
        else:
            # in this implementation if left_child already exists a new node
            # takes it's place and left child of new node directs to
            # the old removed child
            temp = BinaryTree(left_child_value)
            temp.left_child = self.left_child
            self.left_child = temp

    def insert_right_child(self, right_child_value):
        if not self.right_child:
            self.right_child = BinaryTree(right_child_value)
        else:
            temp = BinaryTree(right_child_value)
            temp.right_child = self.right_child
            self.right_child = temp


def pre_order_traverse(node: BinaryTree):
    if not node:
        return
    print(node.root_value)
    pre_order_traverse(node.left_child)
    pre_order_traverse(node.right_child)


def post_order_traverse(node: BinaryTree):
    if node:
        post_order_traverse(node.left_child)
        post_order_traverse(node.right_child)
        print(node.root_value)


def in_order_traverse(node: BinaryTree):
    if node:
        in_order_traverse(node.left_child)
        print(node.root_value)
        in_order_traverse(node.right_child)


if __name__ == '__main__':
    x = BinaryTree("x")
    x.insert_left_child("y_left")
    x.insert_right_child("y_right")
    x.insert_left_child("h1_left")
    x.insert_right_child("h2_right")
    x.insert_left_child("h3_left")
    x.insert_right_child("h3_right")
    pre_order_traverse(x)
    print("*" * 100)
    post_order_traverse(x)
    print("*" * 100)
    in_order_traverse(x)

