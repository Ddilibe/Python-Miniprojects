#imports
import tkinter as tk
from tkinter import messagebox as mBox

class DisplayMessages:
    """
    Abstract class for dispplaying messages when the wrong thing is being inputed
    """
    def info(another_name):
        mBox.showinfo(f"{another_name} Information box", f"This is the {another_name} tab")

    def warning(show_warning):
        mBox.showwarning(f"{show_warning} Warning",f"Incorrect Input\nPlease enter a {show_warning} number")

    def Cwarning(bon,card):
        mBox.showwarning(f"{bon} Warning",f"{card}")

    def Cinfo(name, another_name):
        mBox.showinfo(name,another_name)
