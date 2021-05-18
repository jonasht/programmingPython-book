import pickle, glob


for filename in glob.glob('*.pkl'):
    recFile = open(filename, 'rb')
    record = pickle.load(recFile)
    # print(f'{filename}->\n\t{record}')
    print(f'{filename}->')
    for k, v  in record.items():
        print(f'\t{k.title()}:{v}')
    print('-'*30)
print()

sueFile = open('sue.pkl', 'rb')
print(pickle.load(sueFile)['name'])

