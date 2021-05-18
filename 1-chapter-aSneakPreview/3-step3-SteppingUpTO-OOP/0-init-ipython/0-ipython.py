# coding: utf-8
import shelve
db = shelve.open('people-shelve')
bob = db['bob']
bob['name'].split()[-1]
bob['name'].split()[-1].title()
sue = db['sue']
sue
sue['pay'] *= 1.25
sue['pay']
db['sue'] = sue
db.close()
