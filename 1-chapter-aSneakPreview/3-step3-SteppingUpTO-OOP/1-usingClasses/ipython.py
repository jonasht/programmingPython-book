# coding: utf-8
from person_start import Person
bob = Person('bob', 42)
sue = Person('sue jones', 45)
bob = Person('bob smith', 42)
jonas = Person('jonas t', 26)
people = [bob, sue, jonas]
sue = Person('sue jones', 45, 400000')
sue = Person('sue jones', 45, 400000)
get_ipython().run_line_magic('ls', '')
for person in people:
    print(person.name.title(), ' ', person.pay)
    
people = [bob, sue, jonas]
for person in people:
    print(person.name.title(), ' ', person.pay)
    
x = [(person.name, person.pay) for person in people]
x
[rec.name for rec in people if rec.age >= 45] # sql-ish query
[(rec.age**2 if rec.age >= 45 else rec.age) for rec in people]
