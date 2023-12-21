import random
from turtle import Turtle, Screen
from player import Player
from car import Car

WIDTH, HEIGHT = 800, 600


screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.tracer(0)


player = Player()
car = Car()

car.make_car()

screen.listen()

screen.onkeypress(player.go_up, "Up")

playing_crossy = True
while playing_crossy:
    car.move()
    screen.update()

screen.exitonclick()