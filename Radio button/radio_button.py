import tkinter
from tkinter import *

win = Tk()

var = IntVar()

r1 = Radiobutton(win, text="option1", variable=var, value=1)
r1.pack()
r2 = Radiobutton(win, text="option2", variable=var, value=2)
r2.pack()
r3 = Radiobutton(win, text="option2", variable=var, value=3)
r3.pack()

win.mainloop()
