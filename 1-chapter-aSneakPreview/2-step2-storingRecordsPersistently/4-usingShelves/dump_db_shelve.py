import shelve


db = shelve.open('people-shelve')

for key in db:
    # print(key, '->\n\t', db[key])
    print(f'   {key}->')
    for k, v in db[key].items():
        print(f'\t{k.title():>4}: {v}')
    print('-'*30)

print(db['sue']['name'])
db.close()
