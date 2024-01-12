import tkinter

window = tkinter.Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)


# Label

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label.config(text="new text")

def button_clicked():
    my_label.config(text=user_input)


button = tkinter.Button(text= "Click me", command=button_clicked)
button.pack()

input = tkinter.Entry(width=10)
input.pack()
user_input = input.get()

window.mainloop()
