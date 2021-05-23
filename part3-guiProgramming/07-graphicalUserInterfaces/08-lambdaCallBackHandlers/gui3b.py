import sys
from tkinter import *


widget = Button(
    None,
    text='hello event world\noi mundo event',
    command=(lambda: print('hello lambda world\nola mundo lambda') or sys.exit())
)

widget.pack()
widget.mainloop()