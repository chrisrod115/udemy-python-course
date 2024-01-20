import tkinter

window = tkinter.Tk()
window.title("My first GUI")
window.minsize(500, 300)


# Labels
my_label = tkinter.Label(text="I am a label", font=("Arial", 24))

my_label.pack()


window.mainloop()
