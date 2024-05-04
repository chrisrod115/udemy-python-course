from tkinter import *
import os

script_dir = os.path.dirname(__file__)  # Get the directory where the script itself is located 
desired_working_dir = script_dir  # We want the CWD to be the same as the script's directory
os.chdir(desired_working_dir) 

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_img_fnt = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image= card_img_fnt)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0)
known_button.grid(row=1, column=1)

window.mainloop()
