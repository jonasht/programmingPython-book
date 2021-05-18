


class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
        
if __name__ == '__main__':
    bob = Person('bob smith', 42, 30000, 'software')
    sue = Person('sue jones', 45, 40000, 'hardware')
    jonas = Person('jonas',       27, 1000, 'programmer')

    print(bob.name.title())
    print(bob.pay)
    print()
    
    print(sue.name.title())
    print(sue.pay)
    print()
    
    print(jonas.name.title())
    print(jonas.job.title())