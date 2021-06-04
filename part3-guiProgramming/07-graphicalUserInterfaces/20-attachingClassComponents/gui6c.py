from sys import exit

from tkinter import *
from tkinter.font import names
from gui6 import Ola

class HelloContainer(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.makeWidgets()

    
    def makeWidgets(self):
        Ola(self).pack(side=RIGHT)
        Button(self, text='attach', command=self.quit).pack(side=RIGHT)

if __name__ == '__main__':
    HelloContainer().mainloop()