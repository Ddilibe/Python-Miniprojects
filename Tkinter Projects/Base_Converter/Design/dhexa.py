


#===============================================================================
# Import
#===============================================================================

import tkinter as tk
from tkinter import ttk, Menu, scrolledtext
from Design.Prototype.tablet import TabView


class HexadecimalTabView(TabView):
    """
    Implementing the tab view of the hexadecimal converter
    """
    def __init__(self, Parent):
        """
        Initializing the super class TabView
        """
        super().__init__(Parent, "Hexadecimal Converter")
        self._option = ['Octadecimal','Binary','Denary']
