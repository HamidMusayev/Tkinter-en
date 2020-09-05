from tkinter import *
from tkinter import ttk

win = Tk()
w = ttk.Button(win, text="new button")

w1 = Button(win, text="old button")
w1.pack()
w.pack()
win.mainloop()