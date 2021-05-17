import pickle


dbfile = open('people-pickle', 'rb') # uso mode binario de arquivos em py3...
db = pickle.load(dbfile)

for key in db:
    print(key, '->\n', db[key])
print(db['sue']['name'])
