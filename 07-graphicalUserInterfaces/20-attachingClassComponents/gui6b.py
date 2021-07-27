from sys import exit

from tkinter import *
from gui6 import Ola

parent = Frame(None)
parent.pack()

Ola(parent).pack(side=LEFT)

Button(parent, text='attach', command=exit).pack(side=RIGHT)
parent.mainloop()