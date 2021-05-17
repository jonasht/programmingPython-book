import pickle


dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)
dbfile.close()

db['sue']['pay'] *= 1.10
db['tom']['name'] = 'tolis'


dbfile = open('people-pickle', 'wb')
pickle.dumb(db, dbfile)
dbfile.close()
