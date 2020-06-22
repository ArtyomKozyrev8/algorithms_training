import turtle


def draw_spiral(turt: turtle.Turtle, distance: int) -> None:
    """
    Draws square like spiral
    :param turt: Turtle instance
    :param distance: is integer number
    :return: None
    """
    if distance > 0:
        turt.forward(distance)  # draw line
        turt.right(90.0)  # rotate clockwise 90 degrees
        draw_spiral(turt, distance - 5)
    return  # I decided to put it here explicitly


if __name__ == '__main__':
    t = turtle.Turtle()
    w = turtle.Screen()
    draw_spiral(t, 200)
    w.exitonclick()
