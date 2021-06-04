from user_preferences import bcolor, bfont, bsize


class ThemedButton(Button):
    def __init__(self, parent=None, **configs):
        Button.__init__(self, parent, **configs) # para configurar botao
        self.pack()

        self.config(fg='green', bg='black', font=('caurier', 12), relief=RAISED, bd=5)

class MyButton(ThemedButton):
    def __init__(self, parent, **configs):
        ThemedButton.__init__(self, parent, **configs)

        
MyButton(command=onSpan)
