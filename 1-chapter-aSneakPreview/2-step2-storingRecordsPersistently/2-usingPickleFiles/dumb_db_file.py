from make_db_file import loadDatabase

db = loadDatabase()
for key in db:
    print(key, '=>', db[key])
print()
print(db['sue']['name'])
