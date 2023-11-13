import py
import pytest

from trees import BinaryHeap


@pytest.mark.parametrize(
    "input_",
    [
        ([5]),
        ([5, 9]),
        ([5, 9, 11]),
        ([5, 9, 11, 14]),
        ([5, 9, 11, 14, 18]),
        ([5, 9, 11, 14, 18, 19]),
        ([5, 9, 11, 14, 18, 19, 21]),
        ([5, 9, 11, 14, 18, 19, 21, 33]),
        ([5, 9, 11, 14, 18, 19, 21, 33, 17]),
        ([5, 9, 11, 14, 18, 19, 21, 33, 17, 27]),
        ([5, 7, 11, 14, 9, 19, 21, 33, 17, 27, 18]),
    ]
)
def test_insert(input_) -> None:
    s = BinaryHeap()
    for i in input_:
        s.insert(i)

    assert str(s) == f"BinaryHeap({input_})"
