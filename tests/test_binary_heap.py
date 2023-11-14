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


def test_delete() -> None:
    s = BinaryHeap()
    for i in [5, 9, 11, 14, 18, 19, 21, 33, 17, 27]:
        s.insert(i)

    assert str(s) == "BinaryHeap([5, 9, 11, 14, 18, 19, 21, 33, 17, 27])"

    s.delete() == 5
    assert str(s) == "BinaryHeap([9, 14, 11, 17, 18, 19, 21, 33, 27])"
    s.delete() == 9
    assert str(s) == "BinaryHeap([11, 14, 19, 17, 18, 27, 21, 33])"
    s.delete() == 11
    assert str(s) == "BinaryHeap([14, 17, 19, 33, 18, 27, 21])"
    s.delete() == 14
    assert str(s) == "BinaryHeap([17, 18, 19, 33, 21, 27])"
    s.delete() == 17
    assert str(s) == "BinaryHeap([18, 21, 19, 33, 27])"
    s.delete() == 18
    assert str(s) == "BinaryHeap([19, 21, 27, 33])"
    s.delete() == 19
    assert str(s) == "BinaryHeap([21, 33, 27])"
    s.delete() == 21
    assert str(s) == "BinaryHeap([27, 33])"
    s.delete() == 27
    assert str(s) == "BinaryHeap([33])"
    s.delete() == 33
    assert str(s) == "BinaryHeap([])"
    with pytest.raises(IndexError):
        s.delete()
