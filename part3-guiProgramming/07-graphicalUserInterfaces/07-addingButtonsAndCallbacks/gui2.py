import sys
from tkinter import *
widget = Button(None, text='hello gui world\nola mundo gui', command=sys.exit)
# widgetpt = Button(None, text='ola mundo gui', command=sys.exit)
widget.pack()
widget.mainloop()