import shelve



db = shelve.open('class-shelve')

sue = db['sue'] # puxando
sue.giveRaise(25) # dando aumento 
db['sue'] = sue # mandando de volta

tom = db['tom']
tom.giveRaise(20)
db['tom'] = tom

db.close()

