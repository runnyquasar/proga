import re

fname = input('Введите имя файла: ' + '\n')
with open(fname, 'r' , encoding='utf-8') as f:
    list = f.read()
    list = list.split('\n')

sphere = re.match(r'"Научная сфера", [А-Яа-я]', list)

print(sphere.group(0))



