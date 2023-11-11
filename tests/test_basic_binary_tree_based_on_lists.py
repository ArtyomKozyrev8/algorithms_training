from trees import basic_binary_tree_based_on_lists as basic_tree


def test_basic_binary_tree_based_on_lists() -> None:
    a_tree = basic_tree.make_binary_tree(3)
    assert a_tree == [3, [], []]
    basic_tree.insert_left(a_tree, 4)
    assert a_tree == [3, [4, [], []], []]
    basic_tree.insert_left(a_tree, 5)
    assert a_tree == [3, [5, [4, [], []], []], []]
    basic_tree.insert_right(a_tree, 6)
    assert a_tree == [3, [5, [4, [], []], []], [6, [], []]]
    basic_tree.insert_right(a_tree, 7)
    assert a_tree == [3, [5, [4, [], []], []], [7, [], [6, [], []]]]
    left_child = basic_tree.get_left_child(a_tree)
    assert left_child == [5, [4, [], []], []]
    basic_tree.set_root_val(left_child, 9)
    assert a_tree == [3, [9, [4, [], []], []], [7, [], [6, [], []]]]
    basic_tree.insert_left(left_child, 11)
    assert a_tree == [3, [9, [11, [4, [], []], []], []], [7, [], [6, [], []]]]
    assert basic_tree.get_right_child(basic_tree.get_right_child(a_tree)) == [6, [], []]
