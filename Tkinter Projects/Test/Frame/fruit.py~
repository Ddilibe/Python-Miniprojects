

import tkinter as tk
from tkinter import ttk


class Banana(ttk.Frame):
    
    def __init__(self, Parent):
        super().__init__(Parent)
        self.fra = ttk.LabelFrame(self, text="Pricky Python")
        self.fra.grid(column=0, row=0)
        ttk.Label(self.fra, text="Enter a Number:").grid(column=2, row=1)
        ttk.Button(self.fra, text="Click Me!").grid(column=1, row=1)

class Apple(Banana):

    def __init__(self, Parent):
        super().__init__(Parent)
        self.fra = ttk.LabelFrame(self, text="Monty Python")
        self.fra.grid(column=0,row=0)
        ttk.Button(self.fra, text="Click Me!").grid(column=1, row=1)
        ttk.Label(self.fra, text="Enter a Number: ").grid(column=0, row=1)
