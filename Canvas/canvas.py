import tkinter
from tkinter import *

win = Tk()

c = Canvas(win, height=250, width=300, bg="blue")
coord = 20, 50, 250, 200
arc = c.create_arc(coord, start=0, extent=180, fill="red")
line = c.create_line(10, 10, 200, 200, fill="white")

c.pack()
win.mainloop()
