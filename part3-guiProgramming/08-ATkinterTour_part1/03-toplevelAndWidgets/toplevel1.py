from tkinter import Tk, Button, NoDefaultRoot

NoDefaultRoot()

win1 = Tk()
win2 = Tk()

Button(win1, text='span', command=win1.destroy).pack()
Button(win2, text='span', command=win2.destroy).pack()

win1.mainloop()

