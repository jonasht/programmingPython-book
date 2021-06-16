from tkinter import *
import tkinter
from gui7 import HelloPackage

# chamando tk, obs: tem que chamar tk para funcionar/ nao livro nao eh chamado
root = Tk()

frame = Frame(root)
frame.pack()

Label(frame, text='hello/ ola').pack()

part = HelloPackage(frame)

root.mainloop() # <------------- mainloop aqui tambem
