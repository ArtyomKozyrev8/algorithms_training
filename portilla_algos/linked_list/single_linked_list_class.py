"""
Node - is a composite part of Single Linked List Class

SingleLikedList - represents Single Linked List Class

SingleLinkedListError - is a base Error for all custom errors of the module

SetAfterNthMemberError - error which take place if we are trying to put element in SingleLikedList after element number
which does not exist. Derived from SingleLinkedListError.

SingleLinkedListError - error which take place if we are trying to put element in SingleLikedList before element number
which does not exist. Derived from SingleLinkedListError.
"""


class Node:
    """Node is the class which describes node in single linked list and similar structures"""
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __repr__(self) -> str:
        return f"Node({self.value})"


class SingleLinkedListError(Exception):
    """Base class of SingleLinkedList Errors"""
    pass


class SetAfterNthMemberError(SingleLinkedListError):
    """Raised if we are trying to put element in SingleLikedList after element number which does not exist"""
    pass


class SetBeforeNthMemberError(SingleLinkedListError):
    """Raised if we are trying to put element in SingleLikedList after element number which does not exist"""
    pass


class SingleLikedList:
    """
    SingleLikedList is the class which describes Single Linked List and it's methods
    """
    def __init__(self):
        self.head_node = None  # the first node in the instance
        self.number_of_elements = 0  # number of Nodes in the SingleLikedList

    def __repr__(self) -> str:
        """
        The method not only provide sting presentation of the class, but also checks if there is loop
        inside the instance of the SingleLikedList class.
        :return: string presentation of class instance
        """
        if not self.check_if_loop_in_list():  # we consider looped linked list as incorrect
            r = ""  # this is string presentation of the class
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

    def __len__(self) -> int:
        """Provides number of node in SingleLikedList instance"""
        return self.number_of_elements

    def __iter__(self):
        """Allow to iterate through element of the linked list"""
        cur = self.head_node
        while cur:
            yield cur
            cur = cur.next_node

    def __getitem__(self, item: int) -> Node:
        """Allows to get element of linked list by it's index"""
        if item > len(self) - 1:
            raise IndexError
        if item < 0:
            raise IndexError

        cur_index = 0
        cur = self.head_node
        while cur_index != item:
            cur = cur.next_node
            cur_index += 1
        return cur


    def add_to_head(self, node: Node):
        """
        Adds node to the head of SingleLikedList
        :param node: new node of the instance
        :return:
        """
        assert isinstance(node, Node), "node should be instance of Node class"
        node.next_node = self.head_node
        self.head_node = node
        self.number_of_elements += 1

    def remove_from_head(self) -> None:
        """Removes node if any is available from head of the SingleLikedList"""
        if self.head_node:
            self.head_node = self.head_node.next_node
            self.number_of_elements -= 1

    def add_to_tail(self, node: Node) -> None:
        """
        Adds a new node in the tail of SingleLikedList
        :param node: new node of the instance
        :return:
        """
        assert isinstance(node, Node), "node should be instance of Node class"
        if not self.head_node:
            self.head_node = node
        else:
            cur = self.head_node
            while cur.next_node:
                cur = cur.next_node

            cur.next_node = node

        self.number_of_elements += 1

    def remove_from_tail(self) -> None:
        """Removes node from tail of the list if any is available"""
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

            self.number_of_elements -= 1

    def reverse_list(self) -> None:
        """Reverse nodes in the list"""
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

    def get_nth_element_from_head(self, n: int) -> Node:
        """
        Returns the n-th element of the list from the head if any is available
        :param n: the order number of the element if count from start of the list
        :return: the n-th node from head of the list
        """
        assert isinstance(n, int), "n should be int"
        assert n >= 1, "n should be >= 1"
        cur = self.head_node
        while cur:
            cur = cur.next_node
            n -= 1
            if n == 0:
                return cur
        return

    def get_nth_element_from_tail(self, n: int) -> Node:
        """
        Returns the n-th element of the list from the head if any is available
        :param n: the order number of the element if count from start of the list
        :return: the n-th node from head of the list
        """
        assert isinstance(n, int), "n should be int"
        assert n >= 1, "n should be >= 1"
        n += 1
        cur = self.head_node
        while n:
            if not cur:
                return
            cur = cur.next_node
            n -= 1
        nth_from_head = cur

        cur = self.head_node
        while nth_from_head:
            cur = cur.next_node
            nth_from_head = nth_from_head.next_node
        return cur  # nth from tail element

    def insert_element_after_nth_member(self, node: Node, position: int) -> None:
        """
        Inserts element after the nth element of the list
        :param node: new node we would like to insert in the list
        :param position: the order number of element we would like to put a new node after
        :return:
        """
        assert isinstance(node, Node), "node should be instance of Node class"
        assert isinstance(position, int), "position should be integer"
        assert position >= 1, "position should be >= 1"

        if len(self) < position:
            raise SetAfterNthMemberError(
                f"Length of list is {len(self)}, there is no element {position} to put new element after it"
            )
        cur_index = 0
        cur = self.head_node
        while cur_index < position - 1:
            cur = cur.next_node
            cur_index += 1

        next_node = cur.next_node
        cur.next_node = node
        node.next_node = next_node
        self.number_of_elements += 1

    def insert_element_before_nth_element(self, node: Node, position: int) -> None:
        """
        Inserts element before the nth element of the list
        :param node: new node we would like to insert in the list
        :param position: the order number of element we would like to put a new node before
        :return:
        """
        assert isinstance(node, Node), "node should be instance of Node class"
        assert isinstance(position, int), "position should be integer"
        assert position >= 1, "position should be >= 1"

        if len(self) < position:
            raise SetBeforeNthMemberError(
                f"Length of list is {len(self)}, there is no element {position} to put new element before it"
            )

        if position == 1:
            next_node = self.head_node
            self.head_node = node
            self.head_node.next_node = next_node
        else:
            cur_index = 0
            cur = self.head_node
            while cur_index < position - 1:
                prev_node = cur
                cur = cur.next_node
                cur_index += 1

            node.next_node = cur
            prev_node.next_node = node

        self.number_of_elements += 1


if __name__ == '__main__':
    x = SingleLikedList()
    print(len(x))
    ns = [Node(i) for i in range(1, 15)]
    for i in ns:
        x.add_to_head(i)
    n100 = Node(100)
    x.add_to_tail(n100)
    print(x)
    print(len(x))
    x.reverse_list()
    print(x)
    print(len(x))
    x.remove_from_head()
    x.remove_from_head()
    x.remove_from_tail()
    print(x)
    # print(len(x))
    # print(x.get_nth_element_from_head(11))
    # print(x.get_nth_element_from_tail(3))
    x.insert_element_before_nth_element(Node(1000), 11)
    print(x)
    #for i in x:
        #print(i)
    print(x[12])
    print(len(x))



    #y.add_to_head(Node(100))
    #print(y)
    #y.remove_from_tail()
    #y.reverse_list()
    #print(y)
