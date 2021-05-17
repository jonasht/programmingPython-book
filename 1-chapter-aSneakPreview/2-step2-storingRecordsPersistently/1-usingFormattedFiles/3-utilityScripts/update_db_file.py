from make_db_file import loadDatabase, storeDatabase
db = loadDatabase()
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'tom tolis'
storeDatabase(db)
