from initdata import tom
import shelve


db = shelve.open('people-shelve')
sue = db['sue']
sue['pay'] *= 1.10

# update para no db de cada pessoa
db['sue'] = sue
db['tom'] = tom

db.close()
print('update completed/ update terminado')