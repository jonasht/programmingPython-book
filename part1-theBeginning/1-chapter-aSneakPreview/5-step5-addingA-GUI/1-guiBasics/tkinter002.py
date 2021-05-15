from tkinter import *
from tkinter.messagebox import showinfo

def reply():
    showinfo(title='popup', message='Botão foi apertado')

window = Tk()
botao = Button(window, text='\n    aperte    \n', command=reply)
botao.pack()
window.mainloop()
