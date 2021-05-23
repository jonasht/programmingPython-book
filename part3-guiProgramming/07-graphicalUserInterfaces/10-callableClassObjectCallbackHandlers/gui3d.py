import sys 
from tkinter import *

class HelloCallable:
    def __init__(self):
        self.msg = '=-hello __call __ world-='
        
    def __call__(self): # __call__ run depois quando chamado, funcionando logo depois
        print(self.msg)
        sys.exit()
        

widget = Button(None, text='hello event world', command=HelloCallable())
widget.pack()
widget.mainloop()
