from tkinter import *
from tkinter.messagebox import showinfo


def reply(name):
    showinfo(title='reply/resposta', message=f'hello, {name}\noi, {name}')

top = Tk()
top.title('echo')

# ----------------------------------------
# para funcionar imagem no windows
# top.iconbitmap('pythonImgIco.ico') 

# ----------------------------------------
# linux
img = PhotoImage('pythonImgIco.gif')
top.call('wm', 'iconphoto', top._w, img)
# ----------------------------------------

Label(top, text='enter your name:\nentre com teu nome:').pack(side=TOP)

entd = Entry(top)
entd.pack(side=TOP)

bt = Button(top, text='submt\nenviar', command=lambda: reply(entd.get()))
bt.pack(side=LEFT)

top.mainloop()

