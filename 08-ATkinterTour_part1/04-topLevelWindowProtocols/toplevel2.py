from tkinter import *
root = Tk()

trees = [
    ('the larch', 'light blue'),
    ('the pine', 'light green'),
    ('the giant redwood', 'red')
]

for (tree, color) in trees:
    win = Toplevel(root)
    win.title('cantando......')
    win.protocol('WM_DELETE_WINDOW', lambda:None)
    #win.iconbitmap('')

    msg = Button(win, text=tree, command=win.destroy)
    msg.pack(expand=YES, fill=BOTH)
    msg.config(padx=10, pady=10, bd=10, relief=RAISED)
    msg.config(bg='green', fg=color, font=('times', 30, 'bold italic'))

root.title('titulo')
Label(root, text='menu principal').pack()
Button(root, text='sair de todos', command=root.quit).pack()
root.mainloop()