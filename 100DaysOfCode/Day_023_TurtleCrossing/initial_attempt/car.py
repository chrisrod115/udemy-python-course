import random
from turtle import Turtle

WEST = 180
COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
CARS = []
SHAPE = "square"
SPEED = 2

class Car(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape(SHAPE)
        self.color(random.choice(COLORS))
        self.setheading(WEST)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len= 2)
        
        
    def make_car(self):
        x_cor = random.randint(-250, 250)
        y_cor = random.randint(-250, 250)        
        self.goto(x_cor, y_cor)
        
    
    def move(self):
        self.forward(SPEED)