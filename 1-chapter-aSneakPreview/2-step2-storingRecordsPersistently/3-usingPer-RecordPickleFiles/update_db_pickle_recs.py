import pickle



sueFile = open('sue.pkl', 'rb')
sue = pickle.load(sueFile)
sueFile.close()

sue['pay'] *= 1.10
sueFile = open('sue.pkl', 'wb')
pickle.dump(sue, sueFile)
sueFile.close()
