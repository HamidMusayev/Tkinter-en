import tkinter
from tkinter import *
from tkinter import messagebox

# creating message window
win = Tk()


def hello():
    messagebox.showinfo("from computer", "hello, i am working")


b = Button(win, text="Click me", command=hello)
b.pack()
win.mainloop()
