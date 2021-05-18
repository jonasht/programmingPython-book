import shelve
from person import Person
from manager import Manager


p1 = Person('bob smith', 42, 30000, 'software')
p2 = Person('sue jones', 25, 40000, 'hardware')
p3 = Person('tom tolis', 50, 50000)

db = shelve.open('class-shelve')
db['bob'] = p1
db['sue'] = p2
db['tom'] = p3
db.close()
