f = open("/Users/andreakimov/Desktop/Niggu.txt", encoding="utf-8")
text = f.read()
words = text.split()
a = 0
b = 0 
for x in words:
    a += 1
    if x[-1] == ",":
        b += 1
    elif x[-1] == ".":
        b += 1   
c = a-b
print(int(c/a*100),"% слов без знаков препинания." )
