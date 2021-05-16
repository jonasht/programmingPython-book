# coding: utf-8
bob = dict(name = 'bob smith', age = 42, pay = 30000, job= 'dev')
sue = dict(name = 'sue jones', age = 45, pay = 40000, job = 'hdw')
db = {}
db['bob'] = bob
db['sue'] = sue
db['bob']['name']
db['bob']['name'].title()
db['sue']['pay'] = 50000
db['sue']['pay']
db
import pprint
pprint.pprint(db)
for key in db:
    print(key, '=>', db[key]['name'])
    
for key in db:
    print(key, '=>', db[key]['name'].title())
    
    
for key in db:
    print(key, '=>', db[key]['pay'])
    
    
for key in db:
    print(key, '=>', db[key]['name'].split()[-1])
    db[key]['pay'] *= 1.10
    
    
    

    
    
for record in db.values(): print(record['pay'])
x = [db[key]['name'] for key in db]
x
x = [rec['name'] for rec in db.values()]
x
db['tom'] = dict(name = 'tom', age = 50, job=None, pay = 0)
db['tom']
db['tom']['name']
db['tom']['name'].title()
