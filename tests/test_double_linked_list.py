import pytest

from algorithms.revisited_linked_lists.double_linked_list import DLL


def test_append_tail() -> None:
    s = DLL()
    assert str(s) == "DLL: None"
    s.append_tail(1)
    assert str(s) == "DLL: N(1[None, None])"
    s.append_tail(2)
    assert str(s) == "DLL: N(1[None, 2])=N(2[1, None])"
    s.append_tail(3)
    assert str(s) == "DLL: N(1[None, 2])=N(2[1, 3])=N(3[2, None])"
    s.append_tail(4)
    assert str(s) == "DLL: N(1[None, 2])=N(2[1, 3])=N(3[2, 4])=N(4[3, None])"
    s.append_tail(5)
    assert str(s) == "DLL: N(1[None, 2])=N(2[1, 3])=N(3[2, 4])=N(4[3, 5])=N(5[4, None])"
    s.append_tail(6)
    assert str(s) == "DLL: N(1[None, 2])=N(2[1, 3])=N(3[2, 4])=N(4[3, 5])=N(5[4, 6])=N(6[5, None])"
    s.append_head(0)
    assert str(s) == "DLL: N(0[None, 1])=N(1[0, 2])=N(2[1, 3])=N(3[2, 4])=N(4[3, 5])=N(5[4, 6])=N(6[5, None])"


def test_append_head() -> None:
    s = DLL()
    assert str(s) == "DLL: None"
    s.append_head(1)
    assert str(s) == "DLL: N(1[None, None])"
    s.append_head(2)
    assert str(s) == "DLL: N(2[None, 1])=N(1[2, None])"
    s.append_head(3)
    assert str(s) == "DLL: N(3[None, 2])=N(2[3, 1])=N(1[2, None])"
    s.append_head(4)
    assert str(s) == "DLL: N(4[None, 3])=N(3[4, 2])=N(2[3, 1])=N(1[2, None])"
    s.append_head(5)
    assert str(s) == "DLL: N(5[None, 4])=N(4[5, 3])=N(3[4, 2])=N(2[3, 1])=N(1[2, None])"
    s.append_head(6)
    assert str(s) == "DLL: N(6[None, 5])=N(5[6, 4])=N(4[5, 3])=N(3[4, 2])=N(2[3, 1])=N(1[2, None])"
    s.append_tail(0)
    assert str(s) == "DLL: N(6[None, 5])=N(5[6, 4])=N(4[5, 3])=N(3[4, 2])=N(2[3, 1])=N(1[2, 0])=N(0[1, None])"


def test___getitem__() -> None:
    s = DLL()
    assert str(s) == "DLL: None"
    [s.append_head(i) for i in range(0, 7)]
    assert str(s) == "DLL: N(6[None, 5])=N(5[6, 4])=N(4[5, 3])=N(3[4, 2])=N(2[3, 1])=N(1[2, 0])=N(0[1, None])"

    for i in range(0, 6):
        assert s[i] == 6 - i

    with pytest.raises(IndexError):
        s[7]

    s = DLL()
    with pytest.raises(IndexError):
        s[0]

    s.append_head(1)
    assert s[0] == 1
    with pytest.raises(IndexError):
        s[1]


def test___len__() -> None:
    s = DLL()
    assert len(s) == 0
    for i in range(1, 6):
        s.append_head(i)
        assert len(s) == i


def test___contains__() -> None:
    s = DLL()
    assert (0 in s) is False
    [s.append_head(i) for i in range(0, 7)]
    assert str(s) == "DLL: N(6[None, 5])=N(5[6, 4])=N(4[5, 3])=N(3[4, 2])=N(2[3, 1])=N(1[2, 0])=N(0[1, None])"
    for i in range(0, 7):
        assert (i in s) is True

    assert (7 in s) is False
    assert (10 in s) is False


def test_iteration() -> None:
    s = DLL()
    [s.append_head(i) for i in range(0, 7)]
    assert str(s) == "DLL: N(6[None, 5])=N(5[6, 4])=N(4[5, 3])=N(3[4, 2])=N(2[3, 1])=N(1[2, 0])=N(0[1, None])"

    for j in range(0, 7):
        expected_val = 6
        for cur_val in s:
            assert cur_val == expected_val
            expected_val -= 1


def test_pop_head() -> None:
    s = DLL()
    assert str(s) == "DLL: None"
    with pytest.raises(IndexError):
        s.pop_head()

    s.append_head(1)
    assert str(s) == "DLL: N(1[None, None])"
    assert s.pop_head() == 1
    assert str(s) == "DLL: None"

    [s.append_tail(val) for val in range(1, 5)]
    assert str(s) == "DLL: N(1[None, 2])=N(2[1, 3])=N(3[2, 4])=N(4[3, None])"
    assert s.pop_head() == 1
    assert str(s) == "DLL: N(2[None, 3])=N(3[2, 4])=N(4[3, None])"
    assert s.pop_head() == 2
    assert str(s) == "DLL: N(3[None, 4])=N(4[3, None])"
    assert s.pop_head() == 3
    assert str(s) == "DLL: N(4[None, None])"
    assert s.pop_head() == 4
    assert str(s) == "DLL: None"
    with pytest.raises(IndexError):
        s.pop_head()


def test_pop_tail() -> None:
    s = DLL()
    assert str(s) == "DLL: None"
    with pytest.raises(IndexError):
        s.pop_tail()

    s.append_head(1)
    assert str(s) == "DLL: N(1[None, None])"
    assert s.pop_tail() == 1
    assert str(s) == "DLL: None"

    [s.append_tail(val) for val in range(1, 5)]
    assert str(s) == "DLL: N(1[None, 2])=N(2[1, 3])=N(3[2, 4])=N(4[3, None])"
    assert s.pop_tail() == 4
    assert str(s) == "DLL: N(1[None, 2])=N(2[1, 3])=N(3[2, None])"
    assert s.pop_tail() == 3
    assert str(s) == "DLL: N(1[None, 2])=N(2[1, None])"
    assert s.pop_tail() == 2
    assert str(s) == "DLL: N(1[None, None])"
    assert s.pop_tail() == 1
    assert str(s) == "DLL: None"

    with pytest.raises(IndexError):
        s.pop_tail()


def test_reverse() -> None:
    s = DLL()
    assert str(s) == "DLL: None"
    s.reverse()
    assert str(s) == "DLL: None"

    s.append_head(0)
    assert str(s) == "DLL: N(0[None, None])"
    s.reverse()
    assert str(s) == "DLL: N(0[None, None])"
    s.append_tail(1)
    assert str(s) == "DLL: N(0[None, 1])=N(1[0, None])"
    s.reverse()
    assert str(s) == "DLL: N(1[None, 0])=N(0[1, None])"
    s.append_head(2)
    assert str(s) == "DLL: N(2[None, 1])=N(1[2, 0])=N(0[1, None])"
    s.reverse()
    assert str(s) == "DLL: N(0[None, 1])=N(1[0, 2])=N(2[1, None])"
    s.append_tail(3)
    assert str(s) == "DLL: N(0[None, 1])=N(1[0, 2])=N(2[1, 3])=N(3[2, None])"
    s.reverse()
    assert str(s) == "DLL: N(3[None, 2])=N(2[3, 1])=N(1[2, 0])=N(0[1, None])"
    s.append_head(4)
    assert str(s) == "DLL: N(4[None, 3])=N(3[4, 2])=N(2[3, 1])=N(1[2, 0])=N(0[1, None])"
    s.reverse()
    assert str(s) == "DLL: N(0[None, 1])=N(1[0, 2])=N(2[1, 3])=N(3[2, 4])=N(4[3, None])"
