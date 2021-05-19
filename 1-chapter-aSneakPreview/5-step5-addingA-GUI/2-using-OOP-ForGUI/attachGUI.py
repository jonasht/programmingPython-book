from tkinter import *
from tkinter002 import myGui

mainwin = Tk()
Label(mainwin, text=__name__).pack()

popup = Toplevel()
Label(popup, text='attach\nanexo').pack(side=LEFT)
myGui(popup).pack(side=RIGHT)
mainwin.mainloop()