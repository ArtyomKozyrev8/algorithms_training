"""
Node - is a composite part of Single Linked List Class
SingleLikedList - represents Single Linked List Class
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __repr__(self):
        return f"Node({self.value})"


class SingleLikedList:
    def __init__(self):
        self.head_node = None

    def __repr__(self):
        if not self.check_if_loop_in_list():  # we consider looped linked list as incorrect
            r = ""
            cur = self.head_node
            if not cur:
                return r
            while True:
                if not cur:
                    r += "->" f"{cur}"
                    return r
                if r:
                    r += "->" + f"{cur.value}"
                else:
                    r += f"{cur.value}"
                cur = cur.next_node
        else:
            return "Incorrect linked list! Loop in found!"

    def add_to_head(self, node: Node):
        assert isinstance(node, Node), "node should be instance of Node class"
        node.next_node = self.head_node
        self.head_node = node

    def remove_from_head(self):
        if self.head_node:
            self.head_node = self.head_node.next_node

    def add_to_tail(self, node):
        assert isinstance(node, Node), "node should be instance of Node class"
        if not self.head_node:
            self.head_node = node
        else:
            cur = self.head_node
            while cur.next_node:
                cur = cur.next_node

            cur.next_node = node

    def remove_from_tail(self):
        if self.head_node:
            prev = None
            cur = self.head_node
            while cur.next_node:
                prev = cur
                cur = cur.next_node
            if prev:
                prev.next_node = None
            else:
                self.head_node = None

    def reverse_list(self):
        prev_node = None
        cur = self.head_node
        while cur:
            next_node = cur.next_node
            cur.next_node = prev_node
            prev_node = cur
            cur = next_node
        self.head_node = prev_node

    def check_if_loop_in_list(self) -> bool:
        """
        checks if there is a loop in the list
        :return: True if loop, otherwise False
        """
        slow = self.head_node
        fast = self.head_node
        while fast:
            slow = slow.next_node
            fast = fast.next_node
            if not fast:
                return False
            fast = fast.next_node
            if slow == fast:
                return True
        return False

    def get_nth_element_from_head(self, n: int):
        assert isinstance(n, int), "n should be int"
        assert n >= 1, "n should be >= 1"
        cur = self.head_node
        while cur:
            cur = cur.next_node
            n -= 1
            if n == 0:
                return cur
        return

    def get_nth_element_from_tail(self, n: int):
        assert isinstance(n, int), "n should be int"
        assert n >= 1, "n should be >= 1"
        n += 1
        cur = self.head_node
        while n:
            if not cur:
                return
            cur = cur.next_node
            n -= 1
        nth_from_tail = cur

        cur = self.head_node
        while nth_from_tail:
            cur = cur.next_node
            nth_from_tail = nth_from_tail.next_node
        return cur


if __name__ == '__main__':
    x = SingleLikedList()
    ns = [Node(i) for i in range(1, 15)]
    for i in ns:
        x.add_to_head(i)
    n100 = Node(100)
    x.add_to_tail(n100)
    print(x)
    x.reverse_list()
    print(x)
    x.remove_from_head()
    x.remove_from_head()
    x.remove_from_tail()
    print(x)
    print(x.get_nth_element_from_head(11))
    print(x.get_nth_element_from_tail(3))


    #y.add_to_head(Node(100))
    #print(y)
    #y.remove_from_tail()
    #y.reverse_list()
    #print(y)
