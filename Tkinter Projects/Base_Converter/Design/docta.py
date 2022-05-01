



#=============================================================================
# Import  
#=============================================================================
import tkinter as tk
from tkinter import ttk, Menu, scrolledtext
from Design.Prototype.tablet import TabView

class OctadecimalTabView(TabView):
    """
    Implementing the TabView of the octasdecimal converter
    """
    def __init__(self, Parent):
        """
        Initializing the parent super class TabView
        """
        super().__init__(Parent, "Octadecimal Converter")
        self._dict = {
                'Denary':0,
                'Binary':1,
                'Hexadecimal':2,
                }
