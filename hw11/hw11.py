import re

fname = input('Введите имя файла: ' + '\n')
with open(fname, 'r' , encoding='utf-8') as f:
    l = f.read()
result = re.sub('философия' , 'астрология', l)
result = re.sub('философии' , 'астрологии', l)
result = re.sub('философией' , 'астрологией', l)
result = re.sub('философию' , 'астрологию', l)
result = re.sub('Философию' , 'Астрологию', l)
result = re.sub('Философия' , 'Астрология', l)
result = re.sub('Философии' , 'Астрологии', l)
result = re.sub('Философией' , 'Астрологией', l)

new_name = input('Введите имя нового файла: ' + '\n')
with open (new_name, 'w', encoding = 'utf-8') as f:
    f.write(result)
    
