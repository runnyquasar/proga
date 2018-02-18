import random

with open('oborona.csv', 'r', encoding = 'utf-8') as f:
    pairs = f.readlines()
    
hints = {}

for pair in pairs:
    pair = pair.strip('\ufeff \n')
    hint, word = pair.split(';')
    hints[word] = hint

question = random.choice(list(hints.keys()))
hint = hints[question]

print('Давай проверим, насколько все идет по плану.')
print(hint, '.' * len(hint), sep = '')
answer = input('Ваш ответ: ')

if answer == question:
    print('Молодец! В твоем ответе все как в журнале "Корея" - тоже хорошо!')
else:
    print('Нет, макет все же оказался синльней. ', question)
