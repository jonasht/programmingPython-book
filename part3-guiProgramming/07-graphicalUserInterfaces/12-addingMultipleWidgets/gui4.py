from tkinter import *


def greeting():
    print('hello stdout world/ola mundo stdout')

win = Frame()
win.pack()

Label(win, text='hello container world/ola mundo container').pack(side=TOP)
Button(win, text='hello/ola', command=greeting).pack(side=LEFT)
Button(win, text='quit/sair', command=win.quit).pack(side=RIGHT)

win.mainloop()

