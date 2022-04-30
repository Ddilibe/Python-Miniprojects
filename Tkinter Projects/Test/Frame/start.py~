
import tkinter as tk
from tkinter import ttk 
#from pig import SectionA
from fruit import Apple, Banana
from menu import BaseMenu

class StartGUI(tk.Tk):

    def __init__(self):

        super().__init__()
        self.title("This")
        self.note = ttk.Notebook(self)
        self.note.add(Apple(self.note), text="Apple", padding=20)
        self.note.add(Banana(self.note), text="Banana", padding=20)
        self.note.pack(expand="Yes", fill="both")
        BaseMenu(self)
        self.config(menu=BaseMenu(self))


if __name__ == "__main__":
    app = StartGUI()
    app.mainloop()
