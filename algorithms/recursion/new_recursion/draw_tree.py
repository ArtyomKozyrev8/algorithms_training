from turtle import Turtle, Screen


def draw_tree(step: int, turt: Turtle) -> None:
    if step > 0:
        t.forward(step)
        t.right(20)
        draw_tree(step-15, turt)
        t.left(40)
        draw_tree(step-15, turt)
        t.right(20)
        t.backward(step)


if __name__ == '__main__':
    t = Turtle()
    s = Screen()
    t.color("green")
    t.up()
    t.left(90)
    t.backward(100)
    t.down()
    draw_tree(100, t)
    s.exitonclick()
