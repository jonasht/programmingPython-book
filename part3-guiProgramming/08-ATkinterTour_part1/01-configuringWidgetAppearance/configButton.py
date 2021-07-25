from tkinter import *

import tkinter


bt = Button(text='spam')
bt.pack(padx=20, pady=20)

bt.config(bd=8, relief=RAISED)
bt.config(bg='dark green', fg='gray')

bt.config(font=('helvetica', 20, 'underline italic'))




mainloop()
