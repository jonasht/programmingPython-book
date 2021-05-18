import shelve



db = shelve.open('class-shelve')

for key in db:
    print(key, '->\n    ', db[key].name, db[key].pay)
    
bob = db['bob']
sue = db['sue']
tom = db['tom']

print(bob.last_name())
print(sue.last_name())
print(tom.last_name())