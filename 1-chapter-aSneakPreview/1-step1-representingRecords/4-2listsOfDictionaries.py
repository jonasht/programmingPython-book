# coding: utf-8
get_ipython().run_line_magic('run', '4-1otherWaysToMakeDictionaries.py')
bob
sue
people = [bob, sue]
for person in people:
    print(person['name'], person['pay'], sep=', ')
    
for person in people:
    if person['name'].lower() == 'sue jones':
        print(person['pay'])
        
names = [person['name'] for person in people]
list(map((lambda x: x['name']), people)) 
list(map((lambda x: x['name'].title()), people)) 
person
sum(person for person in people)
sum(person['pay'] for person in people)
print(person['pay'] for person in people)
[print(person['pay'] for person in people)]
[rec['name'] for rec in people if rec['age'] >=45]
[(rec['age'] ** 2 if rec['age'] > 45 else rec['age']) for rec in people]
[(rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people]
G = (rec['name'] for rec in people if rec['age'] >= 45)
next(G)
G = ((rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people)
G.__next__()
for p in people:
    print(p['name'].split()[-1])
    p['pay'] *= 1.10
    
for person in people:
    print(person['pay'])
    
    
