
import tkinter as tk
from tkinter import ttk 
from Design.dbin import BinaryTabView
from Design.Prototype.menu import BaseMenu
from Design.ddin import DenaryTabView
from Design.dhexa import HexadecimalTabView
from Design.docta import OctadecimalTabView

class StartGUI(tk.Tk):

    def __init__(self):

        super().__init__()
        self.title("Base Converter")
        self.note = ttk.Notebook(self)
        self.note.add(BinaryTabView(self.note), text="Binary", padding=20)
        self.note.add(DenaryTabView(self.note), text="Denary", padding=20)
        self.note.add(HexadecimalTabView(self.note), text="Hexadecimal", padding=20)
        self.note.add(OctadecimalTabView(self.note), text="Octadecimal", padding=20)
        self.note.pack(expand="Yes", fill="both")
        BaseMenu(self)
        self.config(menu=BaseMenu(self))


if __name__ == "__main__":
    app = StartGUI()
    app.mainloop()
