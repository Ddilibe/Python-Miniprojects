import tkinter as tk
from tkinter import ttk
from fruit import Apple

class SectionA(ttk.Notebook):

    def __init__(self, win):
        super().__init__(win)
        self.add(Apple, text="Apple")
        self.pack(expand="yes", fill="both")

