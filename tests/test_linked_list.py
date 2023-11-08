import pytest

from revisited_linked_lists import LinkedList


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
    s = LinkedList()
    with pytest.raises(IndexError):
        s.remove_tail()

    [s.append_tail(i) for i in range(1, 3)]
    assert str(s) == "LinkedList: N(1)->N(2)->None"

    val = s.remove_tail()
    assert val == 2
    assert str(s) == "LinkedList: N(1)->None"

    val = s.remove_tail()
    assert val == 1
    assert str(s) == "LinkedList: None"

    with pytest.raises(IndexError):
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


def test___getitem__() -> None:
    s = LinkedList()
    assert str(s) == "LinkedList: None"
    [s.append_head(i) for i in range(1, 6)]
    assert str(s) == "LinkedList: N(5)->N(4)->N(3)->N(2)->N(1)->None"

    for i in range(0, 5):
        assert s[i] == 5 - i

    with pytest.raises(IndexError):
        s[5]

    s = LinkedList()
    with pytest.raises(IndexError):
        s[0]

    s.append_head(1)
    assert s[0] == 1
    with pytest.raises(IndexError):
        s[1]


def test___len__() -> None:
    s = LinkedList()
    assert len(s) == 0
    for i in range(1, 6):
        s.append_head(i)
        assert len(s) == i


def test___contains__() -> None:
    s = LinkedList()
    assert (0 in s) is False
    [s.append_tail(i) for i in range(1, 6)]
    assert str(s) == "LinkedList: N(1)->N(2)->N(3)->N(4)->N(5)->None"
    for i in range(1, 6):
        assert (i in s) is True

    assert (6 in s) is False
    assert (10 in s) is False


def test_iteration() -> None:
    s = LinkedList()
    [s.append_tail(i) for i in range(1, 6)]
    assert str(s) == "LinkedList: N(1)->N(2)->N(3)->N(4)->N(5)->None"

    for j in range(3):
        expected_val = 1
        for cur_val in s:
            assert cur_val == expected_val
            expected_val += 1


def test_remove_index() -> None:
    s = LinkedList()
    [s.append_tail(i) for i in range(0, 6)]
    assert str(s) == "LinkedList: N(0)->N(1)->N(2)->N(3)->N(4)->N(5)->None"

    with pytest.raises(IndexError):
        assert s.remove_index(6)

    assert s.remove_index(0) == 0
    assert str(s) == "LinkedList: N(1)->N(2)->N(3)->N(4)->N(5)->None"

    assert s.remove_index(4) == 5
    assert str(s) == "LinkedList: N(1)->N(2)->N(3)->N(4)->None"

    assert s.remove_index(2) == 3
    assert str(s) == "LinkedList: N(1)->N(2)->N(4)->None"

    with pytest.raises(IndexError):
        assert s.remove_index(6)

    assert s.remove_index(1) == 2
    assert str(s) == "LinkedList: N(1)->N(4)->None"

    assert s.remove_index(1) == 4
    assert str(s) == "LinkedList: N(1)->None"

    assert s.remove_index(0) == 1
    assert str(s) == "LinkedList: None"

    with pytest.raises(IndexError):
        assert s.remove_index(0)

    [s.append_tail(i) for i in range(0, 6)]
    assert str(s) == "LinkedList: N(0)->N(1)->N(2)->N(3)->N(4)->N(5)->None"


def test_insert_index() -> None:
    s = LinkedList()
    s.insert_index(index=0, val=0)
    assert str(s) == "LinkedList: N(0)->None"

    s.insert_index(index=0, val=1)
    assert str(s) == "LinkedList: N(1)->N(0)->None"

    s.insert_index(index=5, val=9)
    assert str(s) == "LinkedList: N(1)->N(0)->N(9)->None"

    s.insert_index(index=0, val=2)
    assert str(s) == "LinkedList: N(2)->N(1)->N(0)->N(9)->None"

    s.insert_index(index=2, val=3)
    assert str(s) == "LinkedList: N(2)->N(1)->N(3)->N(0)->N(9)->None"

    s.insert_index(index=3, val=4)
    assert str(s) == "LinkedList: N(2)->N(1)->N(3)->N(4)->N(0)->N(9)->None"

    s.insert_index(index=1, val=5)
    assert str(s) == "LinkedList: N(2)->N(5)->N(1)->N(3)->N(4)->N(0)->N(9)->None"

    s.insert_index(index=len(s) - 1, val=6)
    assert str(s) == "LinkedList: N(2)->N(5)->N(1)->N(3)->N(4)->N(0)->N(6)->N(9)->None"

    s.insert_index(index=len(s), val=7)
    assert str(s) == "LinkedList: N(2)->N(5)->N(1)->N(3)->N(4)->N(0)->N(6)->N(9)->N(7)->None"


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


def test_is_empty() -> None:
    s = LinkedList()
    assert s.is_empty() is True
    s.append_tail(0)
    assert s.is_empty() is False
    s.append_tail(1)
    assert s.is_empty() is False
