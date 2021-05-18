import shelve
from person import Person

fieldNames = ('name', 'age', 'job', 'pay')

db = shelve.open('class-shelve')

while True:
    key = input('\nkey: ')
    if not key:
        break
    if key in db:
        record = db[key] # update record exixtente 
    else:
        record = Person(nome='?', age='?')
        
    for field in fieldNames:
        currval = getattr(record, field)
        nextText = input(f'[{field}]={currval}\n\tnew: ')
        if nextText:
            setattr(record, field, eval(nextText))
    
    db[key] = record
db.close()

