import re

fname = input('Введите имя файла: ' + '\n')
with open(fname, 'r' , encoding='utf-8') as f:
    l = f.read()
    l = l.split('\n')

for i in range(len(l)):  
    if 'Научная сфера' in l[i]:
        #print(l[i])
        print(re.search('[А-ЯЁ][а-яё]+\s?[А-Яа-яЁё]*', l[i+1]).group())