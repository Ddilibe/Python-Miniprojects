
# Viatal Imports
from Design.Prototype.message import DisplayMessages
from Design.Prototype.menu import BaseMenu
from Formular.bases import Hexadecimal
from Design.dbin import BinaryTabView
import tkinter as tk
from tkinter import ttk, Menu

class Converter(tk.Tk):
    """
        This class is used to launch different aspects of the base converter program.

        This also declares my great advancement in understanding the graphical user interface
    """
    def __init__(self,):
        """
        Initiating the file in a very fun way
        """

        self._first_info = "The Base Converter Program"
        self._second_info = "Welcome to the Base Converter Program"
        super().__init__()
        self.title("Base Converter")
        #self.config(menu = BaseMenu())
        self.menudif()
        self.NoteBook(self)
        self.tab1 = BinaryTabView(self)
        self.Notebook.add(self.tab1, Label="Binary")

    
    def _quit(self,):
        """ Command to sliently close the tkinter program """
        self.quit()
        self.destroy()
        exit()

    def _clear_info(self,):
        """ Method for displaying different messages """
        DisplayMessages.Cinfo(self._first_info, self._second_info)

    def menudif(self,):
        self._menu = Menu(self)
        self.config(menu=self._menu)
        self._filemenu = Menu(self._menu, tearoff=0)
        self._filemenu.add_command(label="Intro", command=self._clear_info)
        self._filemenu.add_command(label="Exit", command=self._quit)
        self._menu.add_cascade(label="File", menu=self._filemenu)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Converter")
    tabControl = ttk.Notebook(root)
    tab1 = BinaryTabView(root)
    tab2 = BinaryTabView(root)
    tabControl.add(tab1, text="Binary")
    tabControl.add(tab1, text="Hexadecimal")
    # This place would include the binary, denary, octadecimal and hexadecimal value converters
    root.mainloop()
