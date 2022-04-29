
#============================================================================
# Import
#============================================================================

import tkinter as tk
from tkinter import ttk, Menu

class BaseMenu(tk.Menu):
    """
    This class reprersentes the menu that is to be contained in the Base Converter Program
    """

    def __init__(self,):
        """
            Initiating the inherited class
        """
        super().__init__()
        self._first_info = "The Base Converter Program"
        self._second_info = "Welcome to the Base Converter Program"
        self._menu = Menu(self,)
        self.config(menu=self._menu)
        self._filemenu = Menu(self._menu, tearoff=0)
        self._filemenu.add_command(label="Intro", command=DisplayMessages.Cinfo(first_info, second_info))
        self._filemenu.add_command(label="Exit", command=self._quit())
        self._menu.add_cascade(label="File", menu=self._filemenu)
        self.configure(menu=self.menu)

        
    def _quit(self,):
        """ Command to sliently close the tkinter program """
        self.quit()
        self.destroy()
        exit()
