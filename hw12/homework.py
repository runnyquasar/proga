import os
import re

allnames = os.listdir('.')
allnames = re.findall('[a-z]+[.][a-z]{2,3}', str(allnames), flags=re.IGNORECASE)
print('Всего найдено файлов:' , len(allnames))
print('Названия файлов:', allnames)


