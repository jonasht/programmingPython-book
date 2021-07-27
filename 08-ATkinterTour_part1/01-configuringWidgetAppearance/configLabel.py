from tkinter import *


root = Tk()
labelfont = ('times', 20, 'bold')


# widget = Label(root, text='hello config world/ ola mundo config')
widget = Label(root, text='hello config world')

widget.config(bg='black', fg='yellow')
widget.config(font=labelfont)
widget.config(height=3, width=20)
widget.pack(expand=YES, fill=BOTH)

root.mainloop()