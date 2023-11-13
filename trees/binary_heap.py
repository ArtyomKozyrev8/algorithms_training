class BinaryHeap:
    """
    self._array = [] is the presentation of the structure, but the array can be shown as a binary tree.

    The idea of the structure is is that root node is always minimum value.

    Moreover, each subtree top value is the minimum value.
    """
    def __init__(self) -> None:
        self._array = []

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self._array})"

    def insert(self, value: int) -> None:
        self._array.append(value)  # append to end of the array
        start_position = len(self._array) - 1
        self._percolate_up(start_position)  # then restruct according to rules!

    def _percolate_up(self, start_position: int) -> None:
        current_position = start_position

        while current_position > 0:  # the root node position is 0 = stop
            parent_position = (current_position - 1) // 2  # calculate parent position of current node

            parent = self._array[parent_position]
            current = self._array[current_position]

            if current < parent:
                self._array[parent_position] = current
                self._array[current_position] = parent
                current_position = parent_position
            else:
                break  # stop here!
