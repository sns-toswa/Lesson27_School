from tkinter import *


root = Tk()
root.title("Цікаві кнопки")
root.geometry("250x200")


def button_red():
    root.config(bg="red")

def button_blue():
    root.config(bg="blue")

def button_plus():
    label_text.config(font="Arial 18")

def button_minus():
    label_text.config(font="Arial 10")

def button_change():
    label_text.config(text="Привіт від Python!")


b_red = Button(text="Червоний колір", command=button_red)
b_red.pack(side=TOP, fill=X)


b_blue = Button(text="Синій колір", command=button_blue)
b_blue.pack(side=TOP, fill=X)

b_plus = Button(text="Збільшити шрифт", command=button_plus)
b_plus.pack(side=TOP, fill=X)

b_minus = Button(text="Зменшити шрифт", command=button_minus)
b_minus.pack(side=TOP, fill=X)

b_change = Button(text="Змінити напис", command=button_change)
b_change.pack(side=TOP, fill=X)

label_text = Label(
    text="Hello, World!",
    font="Arial 12",
    fg="white",
    bg="navy"
)
label_text.pack(side=BOTTOM, fill=X)

root.mainloop()
