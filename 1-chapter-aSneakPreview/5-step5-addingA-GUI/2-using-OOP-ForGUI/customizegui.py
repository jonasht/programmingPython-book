from tkinter import mainloop
from tkinter.messagebox import showinfo
from tkinter002 import myGui

class CustomGui(myGui):
    def reply(self):
        showinfo(title='popup', message='ouch')

if __name__ == '__main__':
    CustomGui().pack()
    mainloop()