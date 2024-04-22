from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_img_fnt = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image= card_img_fnt)

canvas.grid(row=0, column=0)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, bg=BACKGROUND_COLOR, highlightthickness=0)
unknown_button.grid(row=1, column=0)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, bg=BACKGROUND_COLOR, highlightthickness=0)
unknown_button.grid(row=1, column=0)

window.mainloop()
