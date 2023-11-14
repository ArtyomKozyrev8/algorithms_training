class BinaryHeap:
    """
    self._array = [] is the presentation of the structure, but the array can be shown as a binary tree.

    The idea of the structure is that root node is always minimum value.

    Moreover, each subtree top value is the minimum value.
    """
    def __init__(self) -> None:
        self._array = []

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self._array})"

    def __len__(self) -> int:
        return len(self._array)

    def get_min(self) -> int:
        if self._array:
            return self._array[0]

        raise IndexError(f"{self.__class__.__name__} instance is empty!")

    def is_empty(self) -> bool:
        if self._array:
            return True

        return False

    def size(self) -> int:
        return len(self._array)

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

    def delete(self) -> int:
        if self._array:
            min_val = self._array[0]
            if len(self._array) == 1:
                self._array.pop()
            else:
                self._array[0], self._array[-1] = self._array[-1], self._array[0]  # change places before deleting
                # then we start to move the item to bottom
                self._array.pop()  # now remove minimum value from structure
                # we should to remove "big" element from tail back
                # (probably it is max element or close to max)
                self._percolate_down(0)

            return min_val

        raise IndexError(f"{self.__class__.__name__} instance is empty!")

    def _get_min_child_index(self, index: int) -> int:
        max_index = len(self._array) - 1

        left_child_index = 2 * index + 1  # probably out of range
        right_child_index = 2 * index + 2  # probably out of range

        if left_child_index > max_index:
            raise IndexError(
                f"{self.__class__.__name__} instance does not contain item with index {left_child_index}!"
            )

        if right_child_index > max_index:
            min_child_index = left_child_index  # means only one child exists
        else:
            left_child = self._array[left_child_index]
            right_child = self._array[right_child_index]

            if left_child <= right_child:
                min_child_index = left_child_index
            else:
                min_child_index = right_child_index

        return min_child_index

    def _percolate_down(self, start_position: int) -> None:
        current_position = start_position

        # 2 * current_position + 1 this is potential left child position
        # we check if current node have any child
        while 2 * current_position + 1 <= len(self._array) - 1:
            min_child_index = self._get_min_child_index(current_position)
            min_child_value = self._array[min_child_index]
            current_value = self._array[current_position]
            if current_value < min_child_value:
                break
            else:
                self._array[min_child_index] = current_value
                self._array[current_position] = min_child_value
                current_position = min_child_index

        return
