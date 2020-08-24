import tkinter
from tkinter import *

win = Tk()

# we need variables
c1 = IntVar()
c2 = IntVar()

cb = Checkbutton(win, text="Music", offvalue=0, onvalue=1, height=5, width=10, variable=c1)
cb.pack()
cb2 = Checkbutton(win, text="Video", offvalue=0, onvalue=1, height=5, width=10, variable=c2)
cb2.pack()


win.mainloop()
