
#Imports
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")

# Adding a Label
aLabel = ttk.Label(win, text="Enter a Name:")
aLabel.grid(column=0, row=0)

#Button click Event Callback Function
def clickMe():
    action.configure(text="Hello"+name.get())
    aLabel.configure(foreground='red')

# Adding a button
action = ttk.Button(win, text='Click Me!', command=clickMe)
action.grid(column=1, row=1)

# Adding a textbox entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)


win.mainloop()
