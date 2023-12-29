"""
1. Set Background 
    a. done
2. Open Prompt Window
    a. Set the title of the window to show the number of states guessed correctly out of 50 (5) --> done
    b. Prompt user with "What's another states name?" (5) --> done
3. Create a dictionary of states locations and names
    a. Figure out the location of the states shown in the gif. (10) --> done
    b. Map the coordinates with the proper location and name (5) --> --> done
4. State name matches add the state to the map
    a. Loop through dictionary key values and determine if they are a match (10) --> done
    b. If they are add the name of the state on the map. (10) --> done
    c. If guessed a state that is already guessed, prompt user that guess was already made. (15)
    d. Else do not update anything (15)
5. If cancel/done return a result of how many states were guessed
    a. If pressed the cancel button show the states that were guessed and also the final score. (15)

I am trying this new approach to problem solving. Writing out all of the problem and breaking it down by big implementations 
and then splitting them up again. Then I am adding a number that I think I can make the implementation in. For example (5) means
that I can implement this in code in around 5 minutes. 
"""
import pandas as pd
from turtle import Turtle, Screen

class StateGame:
    def __init__(self):
        self.tt = Turtle()
        self.sc = Screen()
        self.sc.setup(900, 700)
        self.sc.bgpic("blank_states_img.gif")
        self.data = pd.read_csv("50_states.csv")
        self.sc.tracer(0)

        self.score = 0
        self.guessed_states = []

    def create_state(self, state_name, x_cor, y_cor):
        self.tt.penup()
        self.tt.hideturtle()
        self.tt.goto(x_cor, y_cor)
        self.tt.write(state_name, align="center", font=('Arial', 10, 'normal'))

    def check_guess(self, guess):
        if guess in self.guessed_states:
            print(f"Already guessed this state: {guess}")
            return False
        return True

    def user_guessing(self):
        user_guess = str(self.sc.textinput(f"Guessed: {self.score}/50", "What's another state's name? ('q' to quit) ")).title()
        if user_guess == 'Q':
            return False
        elif self.check_guess(user_guess):
            for s in self.data.state:
                if s == user_guess:
                    self.score += 1
                    self.guessed_states.append(user_guess)
                    location = self.data.loc[self.data.state == s]
                    x_loc = location["x"].values[0]
                    y_loc = location["y"].values[0]
                    self.create_state(s, x_loc, y_loc)
                    return True
        return True

    def play_game(self):
        guessing = True
        while guessing:
            guessing = self.user_guessing()
            self.sc.update()

        print(f"Final score: {self.score}/50")

# Create an instance of the game and play
game = StateGame()
game.play_game()




