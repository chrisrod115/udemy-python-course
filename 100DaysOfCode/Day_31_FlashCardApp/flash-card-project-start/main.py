import random
from tkinter import *
import pandas as pd
import time
import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.realpath(__file__))

BACKGROUND_COLOR = "#E7E8D1"
FONT_COLOR_1 = "#A7BEAE"
FONT_COLOR_2 = "#B85042"
LANGUAGE_FONT = ("Courier", 30, "italic")
FRENCH_WORD = os.path.join(script_dir, "data", "french_words.csv")

WINDOW_SIZE_X = 900
WINDOW_SIZE_Y = 700

# ------------------------ IMPORT DICTIONARY -------------------------- #
word_list_csv = pd.read_csv(FRENCH_WORD)
rand_num = random.randint(0, 99)

def random_word_generator(trigger):
    eng_word = word_list_csv["English"][rand_num]
    fre_word = word_list_csv["French"][rand_num]
    return eng_word, fre_word

# -------------------------- INITIALIZATION --------------------------- #
START_APP = (1, 1)


# --------------------------- FLIP LOGIC ------------------------------ #

# --------------------------- TIMER LOGIC ----------------------------- #

# -------------------------- BUTTON LOGIC ----------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.configure(background=BACKGROUND_COLOR)
window.minsize(height=WINDOW_SIZE_Y, width=WINDOW_SIZE_X)
window.title("Flash Cards App")

# Canvas
## Flash card front side
flash_card_pic_front = PhotoImage(file=os.path.join(script_dir, "images", "card_front.png"))
flash_card_canvas_front = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0)
flash_card_canvas_front.create_image(400, 263, image=flash_card_pic_front)
flash_card_canvas_front.grid(column=0, row=0)

## Flash card back side
flash_card_pic_back = PhotoImage(file=os.path.join(script_dir, "images", "card_back.png"))
flash_card_canvas_back = Canvas(height=550, width=810, bg=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0)
flash_card_canvas_back.create_image(405, 270, image=flash_card_pic_back)
flash_card_canvas_back.grid(column=1, row=1)

# Labels
## English word
en_language_label = Label(text="eng_word", font=LANGUAGE_FONT)
en_language_label.grid(column=1, row=1)
## French word
fr_language_label = Label(text="fre_word", font=LANGUAGE_FONT)
fr_language_label.grid(column=1, row=1)

# Buttons
## Red incorrect button
wrong_button_pic = PhotoImage(file=os.path.join(script_dir, "images", "wrong.png"))
wrong_button = Button(image=wrong_button_pic, bg=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0)
wrong_button.grid(column=1, row=3)

## Green correct button
right_button_pic = PhotoImage(file=os.path.join(script_dir, "images", "right.png"))
right_button = Button(image=right_button_pic, borderwidth=0, highlightthickness=0, bg=BACKGROUND_COLOR)
right_button.grid(column=2, row=3)

window.mainloop()
