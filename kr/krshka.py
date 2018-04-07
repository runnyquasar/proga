import re

fname = input('Введите имя файла: ' + '\n')
with open(fname, 'r', encoding='utf-8') as f:
    spisok = f.read()
    spipok = spisok.split(' ')
searching = re.search('<body>[0-9A-Za-zА-Яа-яЁё<>\\\/\s=",\-()|]*<\/body>', spisok ).group()

fname1 = input('Введите имя нового файла: ' + '\n')
with open(fname1, 'w', encoding="utf-8") as f:
    newone = f.writelines(print(str(len(searching))))
