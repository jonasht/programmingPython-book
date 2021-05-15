# coding: utf-8
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('run', '1-usingLists.py')
people = [bob, sue]
for person in people:
    print(person)
    
people[1][0]
for person in people:
    print(person[0].split()[-1])
    person[2] *= 1.20 # dar a cada 20 porcento de aumento
    
for person in people: print(person[2])
pays = [person[2] for person in people] # coletar todos os pagamentos
pays
pays = map((lambda x: x[2]), people)
list(pays)
sum(person[2] for person in people)
people.append(['Tom', 50, 0, None])
people
len(people)
people[-1]
people[-1][0]
