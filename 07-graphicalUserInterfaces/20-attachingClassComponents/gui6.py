from tkinter import *


class Ola(Frame):
    def __init__(self, parent = None):
        Frame.__init__(self, parent)
        self.pack()

        self.data = 5
        self.make_widgets()

    def make_widgets(self):
        widget = Button(self, text='hello frame world/ola mundo frame',
                        command=self.massage)
        widget.pack(side=LEFT)

        
    def massage(self):
        self.data +=1
        print(f'hello frame world {self.data}')

if __name__ == '__main__': 
    Ola().mainloop()
