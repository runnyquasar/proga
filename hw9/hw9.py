import re

fname = input('Введите имя файла: ' + '\n') + '.txt'
with open(fname, 'r' , encoding='utf-8') as f:
    list = f.read()

all_results = re.search ('[Вв]ыпил[ аои]|[Вв]ыпив[  |"ши"]| [Вв]ыпить' , list)
all_results1=re.search('[Вв]ыпь[ю]|[Вв]ыпье["шь"|"те"|тм]', list )
all_results2=re.search('[Вв]ыпей[ |"те"]', list)                           
all_results3= re.search('[Вв]ыпит[ |аы|"ый"|"ая"|"ые"]',list)

finall=all_results + all_results1 + all_results2 + all_results3

if finall != 0 :
    print("Найденные словоформы: ", finall)
else:
    print("Ничего не найдено")
