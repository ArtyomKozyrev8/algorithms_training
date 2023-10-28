import turtle


def draw_spiral_from_outer(turtle_: turtle.Turtle, cur_distance: int, step: int = 5) -> None:
    """Draws square spiral, starting from outer side."""
    if cur_distance > 0:
        turtle_.forward(cur_distance)  # draw line
        turtle_.right(90.0)  # rotate clockwise 90 degrees
        draw_spiral_from_outer(turtle_, cur_distance - step)


def draw_spiral_from_inner(
        turtle_: turtle.Turtle, max_distance: int, cur_distance: int, step: int = 5
) -> None:
    """Draws square spiral, starting from inner side."""
    turtle_.color("red")

    if cur_distance < step:
        cur_distance = step

    if cur_distance < max_distance:
        turtle_.forward(cur_distance)  # draw line
        turtle_.right(90.0)  # rotate clockwise 90 degrees
        draw_spiral_from_inner(turtle_, max_distance, cur_distance + step, step)


if __name__ == '__main__':
    t = turtle.Turtle()
    w = turtle.Screen()
    draw_spiral_from_outer(t, 200)
    t.penup()
    t.goto(100, 110)
    t.pendown()
    draw_spiral_from_inner(t, 200, 0, 5)
    w.exitonclick()
