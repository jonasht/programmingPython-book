bob = {'name': 'bob smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'sue jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
tom = {'name': 'tom', 'age': 50, 'pay': 0, 'job': None}


# datebase
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

if __name__ == '__main__':
    for key in db:
        print('  ', key, '=>\n\t', db[key])

