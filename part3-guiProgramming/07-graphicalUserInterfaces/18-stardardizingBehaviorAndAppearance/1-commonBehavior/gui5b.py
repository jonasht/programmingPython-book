from gui5 import HelloButton


class MyButton(HelloButton):
    def callback(self):
        print('ignoring press / ignorar aperto')


if __name__ == '__main__':
    MyButton(
        None, 
        text='hello sublclass world / ola mundo subclass'
        ).mainloop()
