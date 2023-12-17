from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def forward():
    turtle.forward(10)
    
def up():
    new_heading = turtle.heading() + 10
    turtle.setheading(new_heading)

def back():
    turtle.forward(-10)
    
def down():
    new_heading = turtle.heading() - 10
    turtle.setheading(new_heading)

screen.listen()
screen.onkeypress(forward, "Right")
screen.onkeypress(up, "Up")
screen.onkeypress(back, "Left")
screen.onkeypress(down, "Down")

screen.exitonclick()