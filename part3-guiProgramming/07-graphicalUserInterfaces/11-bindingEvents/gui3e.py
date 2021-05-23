import sys
from tkinter import *


def hello(event): # sempre tem que ter event na funcao para o bind funcionar 
    print('press twice to exit/ aperte duas vezes para sair')

def quit(event): # sempre tem de ter event/variavel na funcao para o bind funcionar
    print('hello, I must be going/ola, eu devo ir embora ')
    sys.exit()

widget = Button(None, text='hello event world')
widget.pack()

# bind left mouse click 
widget.bind('<Button-1>', hello) # bind('codigo da tecla/bind',  'funcao')
widget.bind('<Double-1>', quit)

widget.mainloop()


    
    