# coding: utf-8
from person import Person
from manager import Manager
bob = Person('bob smith', 42, 10000)
sue = Person('sue jones', 45, 400000)
tom = Person('tom tolis', 50, 30000)
db = [bob, sue, tom]
for p in db:
    print(p.pay)
    print()
    
    p.giveRaise(10)
    print(p.pay)
    
for p in db:
    print(p.last_name(), '_>', p.pay)
    
get_ipython().run_line_magic('save', 'ipython 1-9')
