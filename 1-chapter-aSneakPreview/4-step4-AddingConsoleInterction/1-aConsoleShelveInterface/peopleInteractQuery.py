import shelve
fieldNames = ('name', 'age', 'job', 'pay')
maxField = max(len(f) for f in fieldNames)

db = shelve.open('class-shelve')

while True:
    key = input('\nKey: ')

    if not key: 
        break
    
    try:
        record = db[key]
    except:
        print(f'no such key: {key}')
        print(f'    sem key: {key}')
    else:
        print('-'*30)
        for field in fieldNames:
            print(f'{field.ljust(maxField).title()} -> {getattr(record, field)}')
    
    
    