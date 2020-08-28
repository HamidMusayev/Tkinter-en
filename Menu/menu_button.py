import tkinter
from tkinter import *

win = Tk()


def nothing():
    file = Toplevel(win)
    button = Button(file, text="do nothing")
    button.pack()


menubar = Menu(win)

filemenu = Menu(menubar)
# adding buttons
filemenu.add_command(label="New window", command=nothing)
filemenu.add_command(label="New file", command=nothing)
filemenu.add_command(label="Open..", command=nothing)
# adding separator
filemenu.add_separator()
filemenu.add_command(label="Save..", command=nothing)
filemenu.add_command(label="Save as..", command=nothing)
filemenu.add_separator()
filemenu.add_command(label="Close", command=win.quit)

# you need to attach filemenu to menubar
menubar.add_cascade(label="File", menu=filemenu)
# you need to config menu to window
win.config(menu=menubar)

win.mainloop()
