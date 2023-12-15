# import turtle
from turtle import Turtle, Screen
# import random
import random as rand

screen = Screen()
tim = Turtle()

tim.hideturtle()
tim.width(20)

for i in range(100):
    rand_angle = rand.choice([0, 90, 180, 270])
    rand_forward = rand.randint(10, 50)
    tim.setheading(rand_angle)
    tim.forward(rand_forward)
    screen.colormode(255)
    tim.color(rand.randint(0, 255), 
            rand.randint(0, 255), 
            rand.randint(0, 255))


screen.exitonclick()