from trees.basic_binary_tree import BinaryTree


def test_binary_tree() -> None:
    s = BinaryTree("a")
    assert str(s) == "BT(a, None, None)"
    s.insert_right("b")
    assert str(s) == "BT(a, None, BT(b, None, None))"
    s.insert_left("c")
    assert str(s) == "BT(a, BT(c, None, None), BT(b, None, None))"
    s.insert_right("d")
    assert str(s) == "BT(a, BT(c, None, None), BT(d, None, BT(b, None, None)))"
    right_child = s.get_right_child()
    right_child.insert_left("e")
    assert str(s) == "BT(a, BT(c, None, None), BT(d, BT(e, None, None), BT(b, None, None)))"
    left_child = s.get_left_child()
    left_child.insert_left("f")
    assert str(s) == "BT(a, BT(c, BT(f, None, None), None), BT(d, BT(e, None, None), BT(b, None, None)))"
    left_child.insert_right("g")
    assert str(s) == "BT(a, BT(c, BT(f, None, None), BT(g, None, None)), BT(d, BT(e, None, None), BT(b, None, None)))"
    assert s.get_value() == "a"
    s.set_value(0)
    assert str(s) == "BT(0, BT(c, BT(f, None, None), BT(g, None, None)), BT(d, BT(e, None, None), BT(b, None, None)))"
