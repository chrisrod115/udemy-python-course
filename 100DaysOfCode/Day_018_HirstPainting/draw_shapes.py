from turtle import Turtle, Screen

tim = Turtle()


def make_shapes():
    for i in range(3,8):
        angle = 360 / i
        for j in range(i):
            tim.right(angle)
            tim.forward(100)

        


make_shapes()
screen = Screen().exitonclick()