import tkinter
from tkinter import *

win = Tk()


def pr():
    print("Hello world")


win.geometry("400x400")
b = Button(win, text="Button", command=pr, padx=30, pady=10, bg="red", activebackground="pink", activeforeground="red", relief=FLAT)
b.place(x=200, y=200)
print(b.cget("bg"))

win.mainloop()

#  pack(), grid(row=1, column=1), place(x=100, y=200)
