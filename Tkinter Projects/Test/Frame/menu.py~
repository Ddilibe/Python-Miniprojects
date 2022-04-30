
#============================================================================
# Import
#============================================================================

import tkinter as tk
from tkinter import ttk, Menu
from message import DisplayMessages

class BaseMenu(tk.Menu):
    """
    This class reprersentes the menu that is to be contained in the Base Converter Program
    """

    def __init__(self,Parent):
        """
            Initiating the inherited class
        """
        super().__init__(Parent)
        self._first_info = "The Base Converter Program"
        self._second_info = "Welcome to the Base Converter Program"
        self._filemenu = Menu(self, tearoff=0)
        self._filemenu.add_command(label="Intro", command=self._intro)
        self._filemenu.add_command(label="Exit", command=self._quit)
        self.add_cascade(label="File", menu=self._filemenu)
        

        
    def _quit(self,):
        """ Command to sliently close the tkinter program """
        self.quit()
        self.destroy()
        exit()

    def _intro(self,):
        DisplayMessages.Cinfo(self._first_info, self._second_info)
