class MyQueueBaseError(Exception):
    pass

class MyQueueEmpty(MyQueueBaseError):
    """Queue is empty error, raised when we try to remove element frm empty MyQueue"""
    pass

class MyQueue:
    """Queue implementatition with the help of list"""
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not (self.items):
            raise MyQueueEmpty("MyQueue is empty exception")
        return self.items.pop()

    def is_empty(self):
        if self.items:
            return False
        return True

    def __repr__(self):
        return f"MyQueue({self.items})"

if __name__ == '__main__':
    x = MyQueue()
    print(x.is_empty())
    x.enqueue(1)
    print(x.is_empty())
    x.enqueue(2)
    x.enqueue(3)
    print(x)
    for i in range(10):
        try:
            x.dequeue()
            print(x)
        except MyQueueBaseError as ex:
            print(ex)
            break
