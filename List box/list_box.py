import tkinter
from tkinter import *

win = Tk()

lb = Listbox(win)
lb.insert(1, "python")
lb.insert(2, "java")
lb.insert(1, "dart")
lb.insert(1, "c++")
lb.insert(1, "c#")
lb.insert(1, "swift")
lb.pack()

win.mainloop()
