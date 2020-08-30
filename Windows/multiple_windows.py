import tkinter
from tkinter import *

# creating multiple windows
window = Tk()

top = Toplevel()
top.title("second")
# for make clickable first window top.grab_set()

window.bind("<FocusIn>", window.focus_set())
window.mainloop()
