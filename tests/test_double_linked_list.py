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


def test_append_head():
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
