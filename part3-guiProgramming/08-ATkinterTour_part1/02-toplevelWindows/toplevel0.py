import sys
from tkinter import Toplevel, Button, Label

# quando eh apertado o botão, fecha tudo
# when the button is pressed, exit all of windows



win1 = Toplevel()
win2 = Toplevel()

Button(win1, text='span', command=sys.exit).pack()
Button(win2, text='span', command=sys.exit).pack()

Label(text='popups').pack()


win1.mainloop()

