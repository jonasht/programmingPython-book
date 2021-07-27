from tkinter import *
from gui6 import Ola

class HelloExtender(Ola):
    def make_widgets(self):
        Ola.make_widgets(self)
        Button(self, text='extend/extendido', command=self.quit).pack(side=RIGHT)

    def message(self):
        print('hello/oi ', self.data)
    
if __name__ == '__main__': 
    HelloExtender().mainloop()
    
        