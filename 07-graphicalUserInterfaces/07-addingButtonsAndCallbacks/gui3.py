import sys
from tkinter import *
root = Tk()
widget = Button(root, text='hello gui world\nola mundo gui', command=sys.exit).pack(side=LEFT)
# widgetpt = Button(None, text='ola mundo gui', command=sys.exit)

root.mainloop()