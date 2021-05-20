from tkinter import *
from tkinter.messagebox import showerror
import shelve


shelveName = 'class-shelve'
fieldNames = ('name', 'age', 'pay')

def makeWidgets():
    global entries
    window = Tk()
    window.title('people shelve')
    form = Frame(window) # frame de window
    form.pack()

    entries = {} # dicionario de entradas/entries

    for (ix, label) in enumerate(('key', ) + fieldNames):
        lb = Label(form, text=label)
        entd = Entry(form)
        lb.grid(row=ix, column=0)
        entd.grid(row=ix, column=1)

    Button(window, text='fetch', command=fetchRecord).pack(side=LEFT)
    Button(window, text='update', command=updateRecord ).pack(side=LEFT)
    Button(window, text='quit', command=window.quit).pack(side=RIGHT)
    return window

def fetchRecord(): 
    key = entries['key'].get()
    
    try:
        record = db['key']
    except:
        showerror(title='error', message='no such key')
    else:
        for field in fieldNames:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))


def updateRecord(): 
    key = entries['key'].get()

    if key in db:
        record = db[key]

    else:
        from person import Person
        record = Person(name='?', age='?')
    
    for field in fieldNames:
        setattr(record, field, eval(entries[field].get()))
    db[key] = record
db = shelve.open(shelveName)
window = makeWidgets()
window.mainloop()
db.close()