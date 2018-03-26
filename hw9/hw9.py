import re

fname = input('Введите имя файла: ' + '\n') + '.txt'
with open(fname, 'r' , encoding='utf-8') as f:
    list = f.read()

all_results = re.findall('[Вв]ыпил[ аои]|[Вв]ыпив[  |"ши"]| [Вв]ыпить' , list)
all_results1= re.findall('[Вв]ыпь[ю]|[Вв]ыпье["шь"|"те"|тм]', list )
all_results2= re.findall('[Вв]ыпей[ |"те"]', list)

finall=all_results + all_results1 + all_results2

if finall != 0 :
    print(finall)
else:
    print("Ничего не найдено")
