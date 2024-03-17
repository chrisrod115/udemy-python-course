from tkinter import *
import pandas as pd
import time

BACKGROUND_COLOR = "#E7E8D1"
FONT_COLOR_1 = "#A7BEAE"
FONT_COLOR_2 = "#B85042"
LANGUAGE_FONT = ("Courier", 30, "italic")

WINDOW_SIZE_X = 900
WINDOW_SIZE_Y = 700

# Keep score/metrics

# Checker for right or wrong answers

# Card flip logic

# Create the timer to flip cards

# Design UI interface
window = Tk()
window.configure(background=BACKGROUND_COLOR)
window.minsize(height=WINDOW_SIZE_Y,width=WINDOW_SIZE_X)
window.title("Flash Cards App")

# Canvas
flash_card_pic_front = PhotoImage(file="./images/card_front.png")
flash_card_canvas_front = Canvas(height=550, width=810, bg=BACKGROUND_COLOR,borderwidth=0, highlightthickness=0)
flash_card_canvas_front.create_image(405, 270, image=flash_card_pic_front)
flash_card_canvas_front.grid(column=0, row=0)
flash_card_canvas_front.create_text(200, 100, text="Eng", font=LANGUAGE_FONT, fill="blue")

flash_card_pic_back = PhotoImage(file="./images/card_back.png")
flash_card_canvas_back = Canvas(height=550, width=810, bg=BACKGROUND_COLOR,borderwidth=0, highlightthickness=0)
flash_card_canvas_back.create_image(405, 270, image=flash_card_pic_back)
flash_card_canvas_back.grid(column=1, row=1)

# Labels
en_language_label = Label(text="English", font=LANGUAGE_FONT)
en_language_label.grid(column=0, row=1)
fr_language_label = Label(text="French", font=LANGUAGE_FONT)
fr_language_label.grid(column=0, row=0)

# Buttons
wrong_button_pic = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_pic, bg=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0)
wrong_button.grid(column=2, row=2)

right_button_pic = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_pic, borderwidth=0, highlightthickness=0, bg=BACKGROUND_COLOR)
right_button.grid(column=3, row=3)

window.mainloop()
