from tkinter import *
from tkinter.messagebox import *


def callback():
    if askyesno('verify', 'do you really want to quit?/queres sair?'):
        showwarning('yes/sim', 'quit not yet implemented')
    else:
        showinfo('no/nao', 'quit has been cancelled')

errmg = 'soory, no spam allowed'
Button(text='quit/sair', command=callback).pack(fill=X)
Button(text='Spam', command=(lambda: showerror('spam', errmg))).pack(fill=X)

mainloop()