from turtle import Turtle
import random as rand
class Food:
    def __init__(self) -> None:
        self.food_location = []
        
    
    def create_food(self):
        location = [rand.randint(-200,200), rand.randint(-200, 200)]
        snack = Turtle(shape="circle")
        snack.color('white')
        snack.penup()
        self.food_location.append(location)
        snack.goto(location)
        