

#Imports 
import tkinter as tk
from tkinter import ttk, Menu, scrolledtext
from tkinter import messagebox as mBox


# Creating an instance
win = tk.Tk()


# Add a title
win.title("Python GUI")

# Create a tab control
tabControl = ttk.Notebook(win)

# Create a tab
tab1 = ttk.Frame(tabControl)

# Add the tab
tabControl.add(tab1, text='Tab 1')

# Pack to make visible
tabControl.pack(expand=1, fill="both")

# Creating a second tab
tab2 = ttk.Frame(tabControl)

# Add the second tab
tabControl.add(tab2, text="Tab 2")

# Putting things into the first tab
# Adding the label frame for the two tabs
monty = ttk.LabelFrame(tab1, text="Monty Python")
snake = ttk.LabelFrame(tab2, text="The Snake")
monty.grid(column=0, row=0, padx=20, pady=20)
snake.grid(column=0, row=0, padx=20, pady=20)

""" 
    This is the first tab section
"""
ttk.Label(monty, text="Enter a name: ").grid(column=0,row=0)
ttk.Label(monty, text=" Choose a Number: ").grid(column=1,row=0)
# Adding the click me button
ttk.Button(monty, text="Click Me!").grid(column=2, row=1)
# Adding a Label
ttk.Label(monty, text="Enter a Name:").grid(column=0, row=0, sticky='W')

#Button click Event Callback Function
def clickMe():
    action.configure(text="Hello"+name.get()+ '' + numberChosen.get())

# Adding a button
ttk.Label(monty, text="Click Me Section").grid(column=2, row=0)
action = ttk.Button(monty, text='Click Me!', command=clickMe)
action.grid(column=2, row=1)
#action.configure(state='disabled')

# Adding a combobox
ttk.Label(monty, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(monty, width=12, textvariable=number, state='readonly')
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

# Adding a textbox entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(monty, width=12, textvariable=name)
nameEntered.grid(column=0, row=1, sticky = tk.W)
nameEntered.focus()


"""
    This is the second tab section
"""
# Creating three checkbuttons
chVarDis = tk.IntVar()
check1= tk.Checkbutton(snake, text='Disabled', variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(snake, text="Unchecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(snake, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

# Radiobutton Globals
COLOR1 = "Blue"
COLOR2 = "Gold"
COLOR3 = "Red"

# Radiobutton Callback
def radCall():
    radSel=radVar.get()
    if radSel == 0:
        snake.configure(text='Blue')
    elif radSel == 1:
        snake.configure(text="Gold")
    elif radSel == 2:
        snake.configure(text="Red")

#Using a scrolled Test control
scrolW = 30
scrolH = 3

scr = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap = tk.WORD)
scr.grid(column=0,sticky=tk.EW,columnspan=3)

# First, we change our radiobutton global variables into a list
colors = ["Blue","Gold","Red"]

# Create three Radiobutton using one variable
radVar = tk.IntVar()

# Next, we are selecting a non-existing index value for radVar.
radVar.set(99)

# Now, we are creating all three Radiobutton widgets within one loop
for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(snake, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)

# Create a container to hold labels
labelsFrame = ttk.LabelFrame(snake, text=" Labels in a Frame")
labelsFrame.grid(column=0, row=7)

# Place labels into the conatiners
ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
ttk.Label(labelsFrame, text="Label2").grid(column=0, row=1)
ttk.Label(labelsFrame, text="Label3").grid(column=0, row=2)

# Using loop to add space around a label
for child in labelsFrame.winfo_children():
    child.grid_configure(padx = 8, pady=4)

# Place cursor into name entry
nameEntered.focus()

""" 
    This is the menu section
"""
# Display a Message Box
# Callback function

def _msgBox():
    #mBox.showinfo('Python Message Info Box',"A python GUI created using tkinter:\nThe year is 5015.")
    #mBox.showwarning('Python Message Warning Box', 'A Python GUI created using tkinter:\nWarning:  There might be a bug in this code')
    #mBox.showerror('Python Message Error Box', 'A Python GUI created using tkinter:\nError: Houston - we DO have a serious problem')
    answer = mBox.askyesno("Python Message Dual Choice Box","Are you sure you really wish to do this?")
    print(answer)

# Fuction to exit the program
def _quit():
    win.quit()
    win.destroy()
    exit()

# Creating the menu bar
menuBar = Menu(win)
win.config(menu=menuBar)

# Assigning a menu item to the menu bar
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)

# Creating and assigning a menu item to the created menu bar
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About", command=_msgBox)
menuBar.add_cascade(label="Help", menu=helpMenu)
# Start GUI
win.mainloop()
