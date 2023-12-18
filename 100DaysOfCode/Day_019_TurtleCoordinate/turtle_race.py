from turtle import Turtle, Screen
import random

WIDTH = 500
HEIGHT = 400
TIM_COORDINATE = [(-230, -100), (-230, -60), (-230, -20), (-230, 20), (-230, 60), (-230, 100)]

screen = Screen()
screen.setup(WIDTH, HEIGHT)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").strip().lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(TIM_COORDINATE[i])
    all_turtles.append(tim)

racing = True

while racing:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            racing = False
            winning_color = turtle.pencolor().lower()
            if winning_color == user_bet:
                print(f"You Won! Winning color = {winning_color.capitalize()}")
            else:
                print(f"You lost! Winning color = {winning_color.capitalize()}")
        random_movement = random.randint(1, 10)
        turtle.forward(random_movement)

screen.exitonclick()
