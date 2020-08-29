from tkinter.colorchooser import askcolor

result = askcolor(title="Tkinter Color Chooser")

print(result)
print(result[0])
print(result[1])

# Another example select color of text
import tkinter
from tkinter import *
from tkinter.colorchooser import askcolor


def callback():
    result = askcolor(title="Tkinter Color Chooser")
    label.configure(fg=result[1])
    print(result[1])


root = Tk()
Button(root, text='Choose Color', command=callback).pack(pady=20)

label = Label(root, text="Color", fg="black")
label.pack()

root.geometry('180x160')
mainloop()
