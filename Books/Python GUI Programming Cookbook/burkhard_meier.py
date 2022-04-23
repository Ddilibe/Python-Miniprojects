
#Imports
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")

# Adding a Label
ttk.Label(win, text="Enter a Name:").grid(column=0, row=0)

#Button click Event Callback Function
def clickMe():
    action.configure(text="Hello"+name.get()+ '' + numberChosen.get())

# Adding a button
ttk.Label(win, text="Click Me Section").grid(column=2, row=0)
action = ttk.Button(win, text='Click Me!', command=clickMe)
action.grid(column=2, row=1)
#action.configure(state='disabled')

# Adding a combobox
ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

# Adding a textbox entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)
nameEntered.focus()

win.mainloop()
