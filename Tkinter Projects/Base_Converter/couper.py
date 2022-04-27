
# Viatal Imports
from Formular.bases import Hexadecimal
from Design.dbin import BinaryTabView
import tkinter as tk
from tkinter import ttk, Menu

if __name__ == '__main__':
    win = tk.Tk()
    win.title("Base Converteewr")
    tabControl = ttk.Notebook(win)
    tab1 = ttk.Frame(tabControl)
    tabControl.add(tab1, text="Binary Converter")
    tabControl.pack(expand=1, fill="both")
    BinaryTabView(tab1)
    win.mainloop()
