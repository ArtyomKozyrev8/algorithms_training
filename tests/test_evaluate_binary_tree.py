import pytest

from trees import build_parse_tree, evaluate_parse_tree


@pytest.mark.parametrize(
    "expression,result",
    [
        ("(1+1)", 2),
        ("(3*(4+5))", 27),
        ("((7+3)*(5-2))", 30),
        ("((3*3)+1)", 10),
        ("((((2+2)+(3+3))*4)+1)", 41),
        ("(1-((((2+2)+(3+3))*4)+1))", -40),
    ],
)
def test_evaluate_binary_tree(expression, result):
    assert evaluate_parse_tree(build_parse_tree(expression=expression)) == result
