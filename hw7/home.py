

def open_f(name):
    fname = input('Введите имя файла на английском: ' + '\n') + '.txt'
    with open(fname, encoding='utf-8') as f:
        list = f.read()
        list = list.split(' ')
    return list


def counter(list):
    count = 0
    for word in list:
        if not  word.endswith('ied') and word.endswith('ed'):
            count += 1
    return count

def counter2(list):
    count= 0
    for word in list:
        if word.endswith('ied'):
            count += 1
    return count


open_f = open_f(list)
counter1 = counter(open_f)
counter21 = counter2(open_f)
print('Словоформ на "-ed": ', counter1 )
print('Словоформ на "-ied": ', counter21 )
