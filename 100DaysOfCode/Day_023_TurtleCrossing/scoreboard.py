from turtle import Turtle

FONT = ("Courier", 24, "normal")
LEVEL_POSITION = (-200, 250)

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(LEVEL_POSITION)
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Level = {self.level}", align="center", font=FONT)


    def increase_level(self):
        self.level += 1
        
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over! Highest Level = {self.level}", align="center", font=FONT)
