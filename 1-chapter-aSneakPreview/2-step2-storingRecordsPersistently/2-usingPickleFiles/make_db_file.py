dbFileName = 'people-file'
ENDDB = 'enddb'
ENDREC = 'endrec'
RECSEP = '=>'

def storeDatabase(db, dbFileName = dbFileName):
    dbfile = open(dbFileName, 'w')
    for key in db:
        print(key, file=dbfile)
        for (name, value) in db[key].items():
            print(name + RECSEP + repr(value), file=dbfile)
        print(ENDREC, file=dbfile)
    print(ENDDB, file=dbfile)
    dbfile.close()

def loadDatabase(dbFileName=dbFileName):
    dbfile = open(dbFileName)
    import sys
    sys.stdin = dbfile
    db = {}
    key = input()

    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
            
        db[key] = rec
        key = input()
    return db

if __name__ == '__main__':
    from initdata import db
    storeDatabase(db)

