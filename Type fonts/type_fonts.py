import tkinter
from tkinter import *

# The following code will only change the Font.
root = Tk()
root.option_add('*Font', '19')
root.geometry("200x150")

label = Label(root, text="Hello World")
label.pack(padx=5, pady=5)

root.mainloop()

# The following code changes only the font type.
import tkinter
from tkinter import *

root = Tk()
root.option_add('*Font', 'Times')
root.geometry("200x150")

label = Label(root, text="Hello World")
label.pack(padx=5, pady=5)

root.mainloop()

# If you want a list of font families,
# you can use the following code.
# It will return a list of different font types.
import tkinter
from tkinter import *
from tkinter import font

root = Tk()
print(font.families())

# Finally, you can change both simultaneously
# by writing both at the same time.
import tkinter
from tkinter import *

root = Tk()
root.option_add('*Font', 'Times 19')
root.geometry("200x150")

label = Label(root, text="Hello World")
label.pack(padx=5, pady=5)

root.mainloop()
