
from tkinter import *

#1================================================================================

def frame(root, side):
    w = Frame(root)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w

def button(root, side, text, command=None):
    w = Button(root, text=text, command=command)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w

#2===============================================================================
class Calculator(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Simple Calculator")
        self.master.iconname("Calc1")
        
#3================================================================================
        display = StringVar()
        Entry(self,relief=SUNKEN, textvariable=display).pack(side=TOP, expand=YES, fill=BOTH)

#4&5==============================================================================
        for key in ("123","456","789","-0."):
            keyF = frame(self, TOP)
            for char in key:
                button(keyF, LEFT, char, lambda w = display, s='%s'%char:w.set(w.get()+s))

#6================================================================================
        opsF = frame(self,TOP)
        for char in "+-*/=":
            if char == '=':
                btn = button(opsF, LEFT, char)
                btn.bind('<ButtonRelease-1>', lambda e, s=self, w=display: s.calc(w), '+')
            else:
                btn = button(opsF, LEFT, char, lambda w = display, c = char: w.set(w.get()+' '+c+' '))
        clearF = frame(self, BOTTOM)
        button(clearF, LEFT,'Clr',lambda w=display: w.set(''))
    
#7================================================================================
    def calc(celf, display):
        try:
            display.set(eval(display.get()))
        except ValueError:
            display.set("Error")



if __name__ == '__main__':
    Calculator().mainloop()
