from person import Person



class Manager(Person):
    def giveRaise(self, percent, bonus=0.1):
        self.pay *= (float('1.' + str(percent)) + bonus)


if __name__ == '__main__':
    tom = Manager(name='tom tolis', age=50, pay=5000)
    
    print(tom.last_name())
    print(tom.pay)

    tom.giveRaise(20)
    print(tom.pay)

        
