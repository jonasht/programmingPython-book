from tkinter import *


class HelloPackage:
    def __init__(self, parent=None):
        self.top = Frame(parent) # embed a frame/ encobrindo uma frame
        self.top.pack()

        self.data = 0
        
        self.make_widgets()
        
    def make_widgets(self):
        Button(self.top, text='bye/adeus/gis la revido', command=self.top.quit).pack(side=LEFT)
        Button(self.top, text='hye, eai, saluton', command=self.message).pack(side=RIGHT)

    def message(self):
        self.data += 1
        print('hello number/oi numero', self.data)

if __name__ == '__main__': 
    a = Tk()
    HelloPackage(a)
    
    a.mainloop()


        
