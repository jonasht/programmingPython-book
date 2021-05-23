import sys
from tkinter import *


class HelloClass:
    def __init__(self):
        widget = Button(None, text='hello event world\nola mundo event', command=self.quit)
        widget.pack()
    
    def quit(self):
        print('hello class method world ')
        sys.exit()
    
HelloClass()
mainloop()
