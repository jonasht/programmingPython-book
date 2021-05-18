from initdata import bob, sue, tom
import pickle

for (key, record) in [('bob', bob), ('tom', tom), ('sue', sue)]:
    recFile = open(key + '.pkl', 'wb')
    pickle.dump(record, recFile)
    recFile.close()

