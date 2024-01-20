from tkinter import *

window = Tk()
window.minsize(300, 100)
window.title("Mile to Km converter")


def convert_to_km():
    miles = float(entry.get())
    conversion = miles * 1.60934
    label_conversion.config(text=f"{conversion}")


# Input miles
entry = Entry(width=10)
entry.grid(column=1, row=0)

label_m = Label(text="Miles")
label_m.grid(column=2, row=0)

label_equal = Label(text="is equal to ")
label_equal.grid(column=0, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

label_conversion = Label(text="0")
label_conversion.grid(column=1, row=1)

# Button
button_calculate = Button(text="Calculate", command=convert_to_km)
button_calculate.grid(column=1, row=2)

window.mainloop()
