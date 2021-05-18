class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name.title()
        self.age = age
        self.pay = pay
        self.job = job
    
    # return ultimo nome
    def last_name(self):
        return self.name.split()[-1]

    # dar aumento salarial
    def giveRaise(self, percent): 
        self.pay *= float('1.' + str(percent))
    
if __name__ == '__main__':
    bob   = Person('bob smith', 42, 3000, 'software')
    sue   = Person('sue jones', 45, 4000, 'hardware')
    jonas = Person('jonas tes', 27, 1000, 'software')

    print(sue.name)
    print(sue.pay)

    sue.giveRaise(10)
    print(sue.pay)

    print(bob.name)
    print(bob.job)

    print(jonas.last_name())
    print(jonas.job)