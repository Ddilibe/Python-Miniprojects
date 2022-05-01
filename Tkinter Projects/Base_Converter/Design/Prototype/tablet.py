#Crearing Imports
from abc import ABCMeta, abstractmethod
import tkinter as tk
from tkinter import ttk
from Design.Prototype.message import DisplayMessages
from Formular.binary import Binary
from Formular.denary import Denary
from Formular.hexa import Hexadecimal
from Formular.octa import Octadecimal

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
        self.secondVar = tk.StringVar()

        #========================================================================

        """ Design of the User Interface """
        self.fra = ttk.LabelFrame(self, text=Nameofthefile)
        self.fra.grid(column=0, row=0)
        self.listin = Nameofthefile.split(' ')
        ttk.Label(self.fra, text=f"Enter A {self.listin[0]} Number: ").grid(column=0,columnspan=2,row=0)
        ttk.Button(self.fra, text="Convert",command=self._calculate).grid(column=2,columnspan=3, row=2)

        """ Design for the dropdown Box"""
        self.tuplist = ['Denary','Hexadecimal','Binary','Octadecimal']
        if self.listin[0] in self.tuplist:
            self.tuplist.remove(self.listin[0])

        self.cbase = ttk.Combobox(self.fra, width=14, textvariable=self.firstVar, state='readonly')
        self.cbase['values']=tuple(self.tuplist)
        self.cbase.grid(column=5, columnspan=6,row=1)
        self.cbase.current(0)

        """ Design for the 'convert to' text """
        ttk.Label(self.fra, text="Convert to").grid(column=2, columnspan=3, row=1)

        """ Design for the Input widget """
        self.ebase = ttk.Entry(self.fra, width=12, textvariable=self.secondVar)
        self.ebase.grid(column=0, row=1, columnspan=2,sticky='NESW')
        self.ebase.focus()

        """ Design for the answer display section """
        self.ans = ttk.Label(self.fra, text="Ans: ").grid(column=0,row=3,sticky=tk.E)
        self.ansSection = ttk.Label(self.fra, text="").grid(column=1, row=3,columnspan=3, sticky=tk.W)
        self._error = {
                'NONUM': 'That is not a number',
                'NOBIN': f'That is not a {self.listin[0]} number',
                'NORAN': 'Numbers is not in range of inputs',
                }
        self._formular = {
                'Denary': Denary,
                'Binary':Binary,
                'Hexadecimal':Hexadecimal,
                'Octadecimal':Octadecimal,
                }

    def _calculate(self):
        self.j = self._dict.get(self.firstVar.get())
        self._mular = self._formular.get(self.listin[0])
        self._j = self._mular(str(self.secondVar.get()),self.j).start()
        if self._j in self._error:
            DisplayMessages.Cwarning(self.listin[0],self._error.get(self._j))
        else:
            self.ansSection = ttk.Label(self.fra, text=(" "*100)).grid(column=1, row=3, columnspan=3)
            self._display_ans(self._j)

    def _display_ans(self, i):
        self.ansSection = ttk.Label(self.fra, text=str(i)).grid(column=1, row=3,columnspan=3)
