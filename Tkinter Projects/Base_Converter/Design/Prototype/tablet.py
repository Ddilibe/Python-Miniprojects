#Crearing Imports
from abc import ABCMeta, abstractmethod
import tkinter as tk
from tkinter import ttk

class TabView(metaclass=ABCMeta):
    """ 
        Tab view prototype for each file for the binary converter
    """

    def __init__(self, tabName, Name_of_class):
        """ 
            Initialization for creating the tab
        """
        self._tabName = tabName
        self._tabsubname = ttk.LabelFrame(self._tabName, text=Name_of_class)
        self._name = tk.StringVar()
        self._option = []
        self._action = ttk.Label(self._tabsubname, text="The answer would be should here").grid(column=1, columnspan=4, row=5)
        ttk.Label(self._tabsubname, text=f"THE {(Name_of_class).upper()} CONVERTER").grid(column=0, columnspan=5, row=0)
        self._enter = ttk.Entry(self._tabsubname,width=18,textvariable=self._name)
        self._enter.grid(column=0, columnspan=3, row=2)
        self._enter.focus()
        ttk.Label(self._tabsubname, text=f"Enter the {Name_of_class} Number:").grid(column=0, columnspan=3, row=1, sticky="NSEW")
        ttk.Button(self._tabsubname, text="Convert", command=self._convert).grid(column=5, row=2)
        ttk.Label(self._tabsubname, text="Choose the number that it is converting to:").grid(column=0, row=3)
        self.radVar = tk.StringVar()
        self.list_options()
    
    def list_options(self,):
        for i in range(len(self._option)):
            tk.Radiobutton(self._tabsubname, text=self._option[i], textvariable=self._radVar, value=i).grid(column=(1+i),row=4, sticky=tk.W)


    @abstractmethod
    def Calculate(self, nammy, num):
        pass

    def _convert(self, ):
        """ Function for calling the convert when the button is clicked """
        name = self._name.get()
        num = self._radVar.get()
        try:
            cal = self.Calculate(name,num)
            self.display_answer(cal)
        except:
            pass

    def display_answer(cal):
        self._action.configure(text=f"Ans: {cal}")
