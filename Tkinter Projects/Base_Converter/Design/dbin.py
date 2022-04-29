
#================================================================================
# Imports
#================================================================================
import tkinter as tk
from tkinter import ttk, Menu, scrolledtext
from Design.Prototype.tablet import TabView


class BinaryTabView(TabView):
    """
    Implementing the tabe view of the binary converter
    """
    def __init__(self, ):
        """
        Initializing the different instances of the TabView
        """
        super().__init__("Binary")
        self._option = ['Denary','Octadecimal','Hexadecimal']
        self.list_options()