# coding: utf-8
bob = dict(name = 'bob smith', age = 24, pay = 3000, job= 'dev')
sue = dict(name = 'sue jones', age = 30, pay= 4000, job = 'hdw')
bob, sue
sue
sue['name'] = 'Sue Jones'
sue['age'] = 45
sue['job'] = 'hardware'
sue['pay'] = 40000
sue
print(f'sue: {sue}')
# using zip()
names = ['name', 'age', 'pay', 'job']
value = ['sue jones', 45, 40000, 'hardware']
values = value[:]
value, values
sue = dict(zip(names, values))
sue
sue = dict(zip(names, values))
sue
fields = ('name', 'age', 'job', 'job')
fields = ('name', 'age', 'job', 'pay')
record = dict.fromkeys(fields, '?')
record
