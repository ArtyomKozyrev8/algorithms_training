import pytest

from algorithms.revisited_linked_lists.singly_linked_list import LinkedList, EmptyLinkedListError


def test_append_head() -> None:
    s = LinkedList()
    assert str(s) == "LinkedList: None"
    [s.append_head(i) for i in range(1, 6)]
    assert str(s) == "LinkedList: N(5)->N(4)->N(3)->N(2)->N(1)->None"


def test_append_tail() -> None:
    s = LinkedList()
    assert str(s) == "LinkedList: None"
    [s.append_tail(i) for i in range(1, 6)]
    assert str(s) == "LinkedList: N(1)->N(2)->N(3)->N(4)->N(5)->None"


def test_remove_head() -> None:
    s = LinkedList()
    with pytest.raises(EmptyLinkedListError):
        s.remove_head()

    [s.append_tail(i) for i in range(1, 3)]
    assert str(s) == "LinkedList: N(1)->N(2)->None"
    val = s.remove_head()
    assert val == 1
    assert str(s) == "LinkedList: N(2)->None"
    val = s.remove_head()
    assert val == 2
    assert str(s) == "LinkedList: None"
    with pytest.raises(EmptyLinkedListError):
        s.remove_head()


def test_remove_tail() -> None:
    s = LinkedList()
    with pytest.raises(EmptyLinkedListError):
        s.remove_tail()

    [s.append_tail(i) for i in range(1, 3)]
    assert str(s) == "LinkedList: N(1)->N(2)->None"

    val = s.remove_tail()
    assert val == 2
    assert str(s) == "LinkedList: N(1)->None"

    val = s.remove_tail()
    assert val == 1
    assert str(s) == "LinkedList: None"

    with pytest.raises(EmptyLinkedListError):
        s.remove_tail()

    s.append_head(0)
    assert str(s) == "LinkedList: N(0)->None"
    s.append_tail(1)
    assert str(s) == "LinkedList: N(0)->N(1)->None"

    val = s.remove_tail()
    assert val == 1
    assert str(s) == "LinkedList: N(0)->None"
    s.append_tail(2)
    assert str(s) == "LinkedList: N(0)->N(2)->None"


def test_get_by_index() -> None:
    s = LinkedList()
    assert str(s) == "LinkedList: None"
    [s.append_head(i) for i in range(1, 6)]
    assert str(s) == "LinkedList: N(5)->N(4)->N(3)->N(2)->N(1)->None"

    for i in range(0, 5):
        assert s.get_by_index(i) == 5 - i

    with pytest.raises(IndexError):
        s.get_by_index(5)

    s = LinkedList()
    with pytest.raises(IndexError):
        s.get_by_index(0)

    s.append_head(1)
    assert s.get_by_index(0) == 1
    with pytest.raises(IndexError):
        s.get_by_index(1)


def test_reverse() -> None:
    s = LinkedList()
    s.reverse()
    assert str(s) == "LinkedList: None"
    [s.append_head(i) for i in range(1, 6)]
    s.reverse()
    assert str(s) == "LinkedList: N(1)->N(2)->N(3)->N(4)->N(5)->None"
    s.append_tail(6)
    assert str(s) == "LinkedList: N(1)->N(2)->N(3)->N(4)->N(5)->N(6)->None"
    s.reverse()
    assert str(s) == "LinkedList: N(6)->N(5)->N(4)->N(3)->N(2)->N(1)->None"
    s.append_head(7)
    assert str(s) == "LinkedList: N(7)->N(6)->N(5)->N(4)->N(3)->N(2)->N(1)->None"
    s.append_tail(0)
    assert str(s) == "LinkedList: N(7)->N(6)->N(5)->N(4)->N(3)->N(2)->N(1)->N(0)->None"
    s.reverse()
    assert str(s) == "LinkedList: N(0)->N(1)->N(2)->N(3)->N(4)->N(5)->N(6)->N(7)->None"
