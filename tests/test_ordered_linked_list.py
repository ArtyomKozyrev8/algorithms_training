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

    assert str(s) == "OrderedLinkedList: N(0)->N(2)->N(2)->N(3)->N(4)->N(6)->N(7)->None"


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

    assert str(s) == "OrderedLinkedList: N(7)->N(6)->N(4)->N(3)->N(2)->N(2)->N(0)->None"


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
