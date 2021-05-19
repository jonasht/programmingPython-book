from tkinter import *
from tkinter.messagebox import showinfo

# criando crasse frame / creating a frame crass
class myGui(Frame):
    def __init__(self, parent=None): 
        Frame.__init__(self, parent)
        botao = Button(self, text='aperte\npress', command= self.reply)
        botao.pack()

    def reply(self):
        showinfo(title='popup', message='botao apertado\nbutton pressed')

if __name__ == '__main__':
    window = myGui()
    window.pack()
    window.mainloop()

    