
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
    def __init__(self,tabName ):
        """
        Initializing the different instances of the TabView
        """
        super().__init__(tabName, "Binary Converter")
        self._dict = {
                "Denary":0,
                "Octadecimal":1,
                "Hexadecimal":2,
                }
