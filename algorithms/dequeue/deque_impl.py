class MyDequeBaseError(Exception):
    """Base error for errors which are associated with class MyDeque"""
    pass

class MyDequeEmptyError(MyDequeBaseError):
    """Indicates that we're trying to get element form empty MyDeque"""
    pass

class MyDeque:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def is_empty(self):
        if len(self.items):
            return True
        return False

    def __repr__(self):
        return f"MyDequeue({self.items})"

    def add_to_front_end(self, item):
        self.items.insert(0, item)

    def add_to_rear_end(self, item):
        self.items.append(item)

    def remove_from_front_end(self):
        if not len(self):
            raise MyDequeEmptyError("The Queue is empty error")
        return self.items.pop(0)

    def remove_from_rear_enf(self):
        if not len(self):
            raise MyDequeEmptyError("The Queue is empty error")
        return self.items.pop()


if __name__ == '__main__':
    x = MyDeque()
    x.add_to_rear_end(1)
    x.add_to_rear_end(2)
    x.add_to_rear_end(3)
    x.add_to_front_end(4)
    x.add_to_front_end(5)
    print(x.remove_from_rear_enf())
    print(x.remove_from_front_end())
    print(x)