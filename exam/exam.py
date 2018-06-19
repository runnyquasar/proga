import os
import re
text = ""
def opens(text):
    direct = "/Users/andreakimov/Desktop/news"
    files = os.listdir(direct)
    for filename in files:
        filepath = os.path.join(direct, filename)
        with open (filepath, encoding = "windows-1251") as f:
            m = f.readlines()
    return m
o = opens(text)
def searching(o):
    o = o.split('\n')
    with open("novy.csv", "w", encoding = 'utf-8') as f:
        l = re.sub("'meta', 'content=', 'name='", '', str(o))
        k = re.sub('""', ',', str(text))
        n = re.findall(r'<,\w,', str(text))
        for n in text:
            f.write(n[1:7])
            f.write('\t')
            
       
    
        f.write 
searching(o)
