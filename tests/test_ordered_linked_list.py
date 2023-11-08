import pytest

from revisited_linked_lists import OrderedLinkedList


def test_append():
    s = OrderedLinkedList(reversed_=False)
    assert str(s) == "OrderedLinkedList: None"
    s.append(2)
    assert str(s) == "OrderedLinkedList: N(2)->None"

    for i in [6, 3, 2, 0, 7, 4]:
        s.append(i)

    assert str(s) == "OrderedLinkedList: N(0)->N(2)->N(2)->N(3)->N(4)->N(6)->N(7)->None"

    s = OrderedLinkedList(reversed_=False)
    for i in [3, 6, 2, 0, 2, 7, 4]:
        s.append(i)

    s.append_head(5)
    s.append_tail(6)

    assert str(s) == "OrderedLinkedList: N(0)->N(2)->N(2)->N(3)->N(4)->N(5)->N(6)->N(6)->N(7)->None"


def test_append_reversed_true():
    s = OrderedLinkedList(reversed_=True)
    assert str(s) == "OrderedLinkedList: None"
    s.append(2)
    assert str(s) == "OrderedLinkedList: N(2)->None"

    for i in [6, 3, 2, 0, 7, 4]:
        s.append(i)

    assert str(s) == "OrderedLinkedList: N(7)->N(6)->N(4)->N(3)->N(2)->N(2)->N(0)->None"

    s = OrderedLinkedList(reversed_=True)
    for i in [3, 6, 2, 0, 2, 7, 4]:
        s.append(i)

    s.append_head(5)
    s.append_tail(6)

    assert str(s) == "OrderedLinkedList: N(7)->N(6)->N(6)->N(5)->N(4)->N(3)->N(2)->N(2)->N(0)->None"


def test___contains__():
    s = OrderedLinkedList(reversed_=False)
    assert str(s) == "OrderedLinkedList: None"
    assert (2 in s) is False
    s.append(2)
    assert str(s) == "OrderedLinkedList: N(2)->None"
    assert (2 in s) is True

    for i in [6, 3, 1, 2, 7, 4, 12, 0]:
        s.append(i)
        assert (i in s) is True

    assert str(s) == "OrderedLinkedList: N(0)->N(1)->N(2)->N(2)->N(3)->N(4)->N(6)->N(7)->N(12)->None"

    assert (-1 in s) is False
    assert (100 in s) is False


def test___contains__reversed():
    s = OrderedLinkedList(reversed_=True)
    assert str(s) == "OrderedLinkedList: None"
    assert (2 in s) is False
    s.append(2)
    assert str(s) == "OrderedLinkedList: N(2)->None"
    assert (2 in s) is True

    for i in [6, 3, 1, 2, 7, 4, 12, 0]:
        s.append(i)
        assert (i in s) is True

    assert str(s) == "OrderedLinkedList: N(12)->N(7)->N(6)->N(4)->N(3)->N(2)->N(2)->N(1)->N(0)->None"

    assert (-1 in s) is False
    assert (100 in s) is False


def test_reverse():
    s = OrderedLinkedList(reversed_=False)
    with pytest.raises(AttributeError):
        s.reverse()


def test_remove_head() -> None:
    s = OrderedLinkedList()
    with pytest.raises(IndexError):
        s.remove_head()

    [s.append_tail(i) for i in range(1, 3)]
    assert str(s) == "LinkedList: N(1)->N(2)->None"
    val = s.remove_head()
    assert val == 1
    assert str(s) == "LinkedList: N(2)->None"
    val = s.remove_head()
    assert val == 2
    assert str(s) == "LinkedList: None"
    with pytest.raises(IndexError):
        s.remove_head()


def test_remove_tail() -> None:
    s = OrderedLinkedList()
    with pytest.raises(IndexError):
        s.remove_tail()

    [s.append_tail(i) for i in [2, 1, 0, 8]]
    assert str(s) == "OrderedLinkedList: N(0)->N(1)->N(2)->N(8)->None"

    val = s.remove_tail()
    assert val == 8
    assert str(s) == "OrderedLinkedList: N(0)->N(1)->N(2)->None"

    val = s.remove_tail()
    assert val == 2
    assert str(s) == "OrderedLinkedList: N(0)->N(1)->None"

    s = OrderedLinkedList()
    with pytest.raises(IndexError):
        s.remove_tail()

    s.append_head(0)
    assert str(s) == "OrderedLinkedList: N(0)->None"
    s.append_tail(1)
    assert str(s) == "OrderedLinkedList: N(0)->N(1)->None"

    val = s.remove_tail()
    assert val == 1
    assert str(s) == "OrderedLinkedList: N(0)->None"
    s.append_tail(2)
    assert str(s) == "OrderedLinkedList: N(0)->N(2)->None"


def test_remove_head() -> None:
    s = OrderedLinkedList()
    with pytest.raises(IndexError):
        s.remove_head()

    [s.append_tail(i) for i in range(1, 3)]
    assert str(s) == "OrderedLinkedList: N(1)->N(2)->None"
    val = s.remove_head()
    assert val == 1
    assert str(s) == "OrderedLinkedList: N(2)->None"
    val = s.remove_head()
    assert val == 2
    assert str(s) == "OrderedLinkedList: None"
    with pytest.raises(IndexError):
        s.remove_head()


def test_insert_index() -> None:
    s = OrderedLinkedList()
    with pytest.raises(AttributeError):
        s.insert_index(0, 3)


def test_remove_index() -> None:
    s = OrderedLinkedList()
    [s.append_tail(i) for i in range(0, 6)]
    assert str(s) == "OrderedLinkedList: N(0)->N(1)->N(2)->N(3)->N(4)->N(5)->None"

    with pytest.raises(IndexError):
        assert s.remove_index(6)

    assert s.remove_index(0) == 0
    assert str(s) == "OrderedLinkedList: N(1)->N(2)->N(3)->N(4)->N(5)->None"

    assert s.remove_index(4) == 5
    assert str(s) == "OrderedLinkedList: N(1)->N(2)->N(3)->N(4)->None"

    assert s.remove_index(2) == 3
    assert str(s) == "OrderedLinkedList: N(1)->N(2)->N(4)->None"

    with pytest.raises(IndexError):
        assert s.remove_index(6)

    assert s.remove_index(1) == 2
    assert str(s) == "OrderedLinkedList: N(1)->N(4)->None"

    assert s.remove_index(1) == 4
    assert str(s) == "OrderedLinkedList: N(1)->None"

    assert s.remove_index(0) == 1
    assert str(s) == "OrderedLinkedList: None"

    with pytest.raises(IndexError):
        assert s.remove_index(0)

    [s.append_tail(i) for i in range(0, 6)]
    assert str(s) == "OrderedLinkedList: N(0)->N(1)->N(2)->N(3)->N(4)->N(5)->None"


def test_iteration() -> None:
    s = OrderedLinkedList()
    [s.append_tail(i) for i in range(1, 6)]
    assert str(s) == "OrderedLinkedList: N(1)->N(2)->N(3)->N(4)->N(5)->None"

    for j in range(3):
        expected_val = 1
        for cur_val in s:
            assert cur_val == expected_val
            expected_val += 1


def test___getitem__() -> None:
    s = OrderedLinkedList()
    assert str(s) == "OrderedLinkedList: None"
    [s.append_head(i) for i in range(1, 6)]
    assert str(s) == "OrderedLinkedList: N(1)->N(2)->N(3)->N(4)->N(5)->None"

    for i in range(1, 6):
        assert s[i - 1] == i

    with pytest.raises(IndexError):
        s[5]

    s = OrderedLinkedList()
    with pytest.raises(IndexError):
        s[0]

    s.append_head(1)
    assert s[0] == 1
    with pytest.raises(IndexError):
        s[1]