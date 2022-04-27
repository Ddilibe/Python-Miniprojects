
#Imports 
import tkinter as tk
from tkinter import ttk, Menu, scrolledtext
from Design.Prototype.tablet import TabView
from Design.Prototype.message import DisplayMessages
from Formular.binary import Binary

class BinaryTabView(TabView, DisplayMessages):
    

    def __init__(self,tabControl):
        """
            Initiating the superclass for binary tabview
        """
        super().__init__(tabControl, "Binary")
        self.main_list = ['Denary','Octadecimal','Hexadecimal']
        for i in self.main_list:
            self._option.append(i)

    def Calculate(self, nammy, num):
        j = Binary(nammy,num)
        while j in ["NOBIN","NORAN","NONUM"]:
            if j == "NOBIN":
                DisplayMessages.Cwarning("Binary","That is not a Binary Number")
            if j == "NORAN":
                DisplayMessages.Cwarning("Binary", "The Number is not acceptable")
            if j == "NONUM":
                DisplayMessages.Cwarning("Binary","That is not a number at all")
            j = Binary(nammy, num)
        return j

