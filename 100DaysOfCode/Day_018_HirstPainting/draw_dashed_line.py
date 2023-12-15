from turtle import Turtle, Screen

tim = Turtle()


def draw_dashed_line():
    for _ in range(15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


draw_dashed_line()
screen = Screen().exitonclick()
