class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def isValidBST(root: Node) -> bool:
    minV = - 100000000000
    maxV = 10000000000000

    def check_if_bst(node, minV, maxV):
        if node:
            if node.right:
                if node.val >= node.right.val or node.right.val > maxV:
                    print("A")
                    return False

            if node.left:
                if node.val <= node.left.val or node.left.val < minV:
                    print("A")
                    return False

            check_if_bst(node.right, node.val + 1, maxV)
            check_if_bst(node.left, minV, node.val - 1)

    r = check_if_bst(root, minV, maxV)
    if not r:
        return True
    return r


if __name__ == '__main__':
    x = Node(10)
    x.left = Node(5)
    x.right = Node(15)
    x.right.right = Node(20)
    x.right.left = Node(6)
    print(isValidBST(x))


