# coding: utf-8
bob = {'name': {'first': 'bob', 'last': 'smith'},
       'age': 42,
       'job': ['software', 'writing'],
       'pay': [40000, 50000]}
bob2
bob2 = {'name': {'first': 'bob', 'last': 'smith'},
       'age': 42,
       'job': ['software', 'writing'],
       'pay': [40000, 50000]}
bob2
bob2['name']
bob
bob2['pay']
bob2['pay'][1]
for job in bob2['job']: print(job)
for job in bob2['job']: print(job.title())
bob2['job'][-1]
bob2['job'][-1].upper()
bob2['job'].append('janitor') # colocando um novo job para bob
bob2
