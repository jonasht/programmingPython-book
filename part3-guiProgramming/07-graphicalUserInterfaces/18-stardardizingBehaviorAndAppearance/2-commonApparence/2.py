from user_preferences import bcolor, bfont, bsize


class ThemedButton(Button):
    def __init__(self, parent=None, **configs):
        Button.__init__(self, parent, **configs) # para configurar botao
        self.pack()

        self.config(fg='green', bg='black', font=('caurier', 12), relief=RAISED, bd=5)
    

b1 = ThemedButton(text='span', command='onSpan')
b2 = ThemedButton(text='eggs / ovos')
b2.pack(expand=YES, fill=BOTH)