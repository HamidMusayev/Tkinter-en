import tkinter
from tkinter import *

win = Tk()

frame = Frame(win)
frame.pack()

frame2 = Frame(win)
frame2.pack(side=BOTTOM)

blueButton = Button(frame, text="Blue Button", fg="blue")
blueButton.pack(side=LEFT)
redButton = Button(frame, text="Red Button", fg="red")
redButton.pack(side=LEFT)
greenButton = Button(frame, text="Green Button", fg="green")
greenButton.pack(side=RIGHT)

blackButton = Button(frame2, text="Black Button", fg="black")

win.mainloop()
