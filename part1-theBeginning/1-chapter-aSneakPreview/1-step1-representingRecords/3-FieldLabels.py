# coding: utf-8
get_ipython().run_line_magic('run', '2-aDataBaseList.py')
get_ipython().run_line_magic('ls', '')
bob
NAME, AGE, PAY = range(3)
bob = ['Bob smith', 42, 10000]
bob[NAME]
PAY, bob[PAY]
bob
bob = [['name', 'bob smith'], ['age', 45], ['pay', 10000]]
sue [['name', 'sue Jones'], ['age', 60], ['pay', 20000]]
sue = [['name', 'sue Jones'], ['age', 60], ['pay', 20000]]
bob
jonas = [['jonas', 'teixeira'], ['age', 50], ['pay', 10000]]
people
people = [bob, sue, jonas]
for person in people:
    print(person[0][1], person[2][1]) # nome a pegamento
    
jonas
sue
jonas = [['name', 'jonas teixeira'], ['age', 50], ['pay', 10000]]
for person in people:
    print(person[0][1], person[2][1])
    
[person[0][1] for person in people] 
people
people = [bob, sue, jonas]
for person in people:
    print(person[2][1].split()[-1])
    person[2][1] *= 1.10
    
for person in people:
    print(person[2][1].split()[-1])
    
    person[2][1] *= 1.10
    
for person in people:
    print(str(person[2][1]).split()[-1])
    person[2][1] *= 1.10
    
    
for person in people:
    print(str(person[2][1]).split()[-1])
    #person[2][1] *= 1.10
    
    
[person[0][1] for person in people]
for person in people:
    for (name, value) in person:
        if name == 'name': print(value)
        
for person in people:
    for (name, value) in person:
        if name == 'name': print(value.title())
        
        
def field(record, label):
    for (fname, fvalue) in record:
        if fname == label:
            return fvalue
            
field(bob, 'name')
field(bob, 'pay')
field(bob, 'age')
for rec in people:
    print(field(rec, 'age'))
    
