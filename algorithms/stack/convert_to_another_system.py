from enum import Enum
from algorithms.stack.stack_implementation import Stack


class CalcSystem(Enum):
    SIXTEEN = 16
    OCT = 8
    BIN = 2


def convertor(x: int, d: CalcSystem) -> str:
    assert isinstance(x, int), "x should be integer"
    assert x >= 0, "x should be >= 0"
    assert isinstance(d, CalcSystem), "d should be CalcSystem instance"

    if x == 0 or x == 1:
        return str(x)

    sixteen_system_dict = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
                           10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

    d = d.value
    s = Stack()
    while x >= d:
        t = x // d
        if d != 16:
            s.add(x - t * d)
        else:
            s.add(sixteen_system_dict[x - t * d])
        x = t
    if d != 16:
        s.add(x)
    else:
        s.add(sixteen_system_dict[x])

    result = ""
    if d != 16:
        while not s.is_empty():
            result += str(s.pop())
    else:
        while not s.is_empty():
            result += s.pop()

    return result


if __name__ == '__main__':
    test = [255, 3, 10, 12, 15, 16, 24, 0, 1, 99, 7, 8]
    res = []
    for t in test:
        res.append((convertor(t, CalcSystem.SIXTEEN), convertor(t, CalcSystem.OCT), convertor(t, CalcSystem.BIN),))
    for i, j in zip(test, res):
        print(f"{i}: {j}")








