class StackEmpty(Exception):
    pass


class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        """remove element from stack if stack is not empty"""
        if not self.is_empty():
            return self.items.pop()
        raise StackEmpty("Stack is Empty")

    def peek(self):
        """show element in the top of Stack"""
        return self.items[-1]

    def add(self, item):
        """Add item to the top of Stack"""
        return self.items.append(item)

    def is_empty(self):
        """Check if Stack is empty"""
        return self.items == []

    def __len__(self):
        return len(self.items)


if __name__ == '__main__':
    x = Stack()
    x.add(1)
    x.add(2)
    x.add(3)
    print(x.peek())
    print(x.is_empty())
    x.pop()
    print(x.peek())
    print(len(x))
