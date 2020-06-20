from algorithms.linked_list.new_linked_list.node import LListNode


class UnorderedListBaseError(Exception):
    """UnorderedList Base Error Class"""
    pass


class UnorderedListEmptyError(UnorderedListBaseError):
    """Is raised when we try to remove element from empty UnorderedList"""
    pass


class UnorderedListIndexOutOfRange(UnorderedListBaseError):
    """Is raised when we try to get nonexisted index from list"""
    pass


class UnorderedList:
    """Unordered List implementation based on Liked List"""
    def __init__(self):
        self.head = None

    def is_empty(self):
        """Checks if the list is empty"""
        if self.head:
            return False
        return True

    def __len__(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.get_next()
        return count

    def __repr__(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(str(curr.get_value()))
            curr = curr.get_next()
        return f"UnorderedList({', '.join(elements)})"

    def __getitem__(self, item: int):
        """Returns element item by its index, indexes are integer from 0 to len - 1"""
        if item >= len(self) or item < 0:
            raise UnorderedListIndexOutOfRange("Index out of range error")
        curr = self.head
        while item > 0:
            curr = curr.get_next()
            item -= 1
        return curr.get_value()

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.get_value()
            curr = curr.get_next()

    def pop_based_on_index(self, index: int):
        """Remove element with the certain index out of list"""
        if index < 0 or index >= len(self):
            raise UnorderedListIndexOutOfRange("Index out of range")
        curr = self.head
        next_node = None
        prev_node = None
        if index == 0:
            self.head = curr.get_next()
        else:
            while index > 0:
                prev_node = curr
                curr = curr.get_next()
                next_node = curr.get_next()
                index -= 1
            else:
                prev_node.set_next(next_node)
        return curr.get_value()

    def append_to_head(self, value):
        """Appends element to the head of the list"""
        temp = LListNode(value)
        temp.set_next(self.head)
        self.head = temp

    def append_to_tail(self, value):
        """Appends element to tail of the list"""
        if not self.head:
            self.head = LListNode(value)
        else:
            curr = self.head
            while curr:
                if not curr.get_next():
                    curr.set_next(LListNode(value))
                    break
                curr = curr.get_next()

    def pop_from_head(self):
        """Removes element from the head of the list"""
        if not self.head:
            raise UnorderedListEmptyError("Can't pop from empty UnorderedList")
        temp = self.head.get_value()
        next_node = self.head.get_next()
        self.head = next_node
        return temp

    def pop_from_tail(self):
        """Removes element from the tail of the list"""
        if not self.head:
            raise UnorderedListEmptyError("Can't pop from empty UnorderedList")
        curr = self.head
        prev = None
        while curr:
            temp = curr.get_value()
            if not curr.get_next():
                if prev:
                    prev.set_next(None)
                else:
                    self.head = None
                return temp
            prev = curr
            curr = curr.get_next()
        return curr.get_value()

    def search(self, item):
        """Search for element in the list equal to item, if it founds it - returns True"""
        curr = self.head
        while curr:
            if curr.get_value() == item:
                return True
            curr = curr.get_next()
        return

    def get_index_of_item(self, item):
        """Search for item in the list, if it exists, returns it's value, otherwise returns None"""
        curr = self.head
        index = 0
        while curr:
            if item == curr.get_value():
                return index
            curr = curr.get_next()
            index += 1
        return None

    def remove_item(self, item):
        """Removes element from the list if it is equal to item"""
        curr = self.head
        prev = None
        while curr:
            if curr.get_value() == item:
                next_node = curr.get_next()
                if prev:
                    prev.set_next(next_node)
                else:
                    self.head = next_node  # remove from head margin case
                print(f"Element {item} was removed. Now: {self}")
                break
            prev = curr
            curr = curr.get_next()
        else:
            print(f"Nothing was removed. Item: {item}. Now: {self}")

    def insert_into_position(self, item, index: int) -> None:
        """
        Insert item into the required position. If index out of list range error is raised.
        :param item: some value to add to list
        :param index: index in list where we would like to put elemement
        :return: None
        """
        if index > len(self) or index < 0:
            raise UnorderedListIndexOutOfRange("Index out of list range")
        prev = None
        cur = self.head
        while index > 0:
            prev = cur
            cur = cur.get_next()
            index -= 1
        if prev:
            temp = LListNode(item)
            temp.set_next(cur)
            prev.set_next(temp)
        else:
            temp = LListNode(item)
            temp.set_next(cur)
            self.head = temp


if __name__ == '__main__':
    x = UnorderedList()
    print(x.search(10))
    for i in range(0, 6):
        x.append_to_head(i)
        print(f"{x} Len {len(x)} Empty {x.is_empty()}")
    print(x.search(5))
    print(x.search(9))
    for i in range(0, 6):
        t = x.pop_from_head()
        print(f"{x} Len {len(x)} Empty {x.is_empty()} Poped {t}")
    y = UnorderedList()
    y.remove_item(1)
    for i in range(0, 6):
        y.append_to_head(i)
    y.remove_item(0)
    y.remove_item(5)
    y.remove_item(2)
    y.remove_item(7)
    print("*" * 100)
    for i in range(0, 3):
        t = y.pop_from_tail()
        print(f"{y} Len {len(x)} Empty {y.is_empty()} Poped {t}")
    print("*" * 100)
    for i in range(0, 6):
        x.append_to_tail(i)
        print(f"{x} Len {len(x)} Empty {x.is_empty()}")
    for i in range(0, 6):
        print(x[i])
    print("*" * 100)
    for j in x:
        print(j)
    for i in UnorderedList():
        print(i)
    print(f"Index of item: {x.get_index_of_item(10)}")
    print(x)
    x.insert_into_position(10, 0)
    print(x)
    x.insert_into_position(20, 1)
    print(x)
    x.insert_into_position(30, 3)
    print(x)
    x.insert_into_position(40, 8)
    print(x)
    x.insert_into_position(50, 10)
    print(x)
    print("*" * 100)
    x.pop_based_on_index(0)
    print(x)
    x.pop_based_on_index(9)
    print(x)
    x.pop_based_on_index(3)
    print(x)
    z = UnorderedList()
    z.append_to_head(10)
    z.pop_based_on_index(0)
    print(z)
