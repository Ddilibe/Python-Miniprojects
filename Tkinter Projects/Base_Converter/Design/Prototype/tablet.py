#Crearing Imports
from abc import ABCMeta, abstractmethod
import tkinter as tk
from tkinter import ttk

class TabView(ttk.Frame):
    """ 
        Tab view prototype for each file for the binary converter
    """

    def __init__(self, Parent, Nameofthefile):
        """ 
            Initialization for creating the tab
        """
        super().__init__(Parent)

        #========================================================================
        # Declaring variables
        self.firstVar = tk.StringVar()

        #========================================================================
        # Design of the User Interface
        self.fra = ttk.LabelFrame(self, text=Nameofthefile)
        self.fra.grid(column=0, row=0)
        self.listin = Nameofthefile.split(' ')
        ttk.Label(self.fra, text=f"Enter A {self.listin[0]} Number: ").grid(column=0,columnspan=2,row=0)
        ttk.Button(self.fra, text="Convert").grid(column=2,columnspan=1, row=2)

        self.tuplist = ['Denary','Hexadecimal','Binary','Octadecimal']
        if self.listin[0] in self.tuplist:
            self.tuplist.remove(self.listin[0])

        self.cbase = ttk.Combobox(self.fra, width=14, textvariable=self.firstVar, state='readonly')
        self.cbase['values']=tuple(self.tuplist)
        self.cbase.grid(column=5, columnspan=2,row=1)
        self.cbase.current(0)
        for i in self.cbase['values']:
            print(i)
