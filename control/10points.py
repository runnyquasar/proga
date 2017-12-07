lines=[]
with open("/Users/andreakimov/Desktop/freq.txt", encoding="utf-8") as f:
    lines=f.readlines()
    user_word=input('Введите слово: ')
    for line in lines:
        form=line.split('|')
        
        if user_word in lines:
            print(form[1:2])
        else:
            print('в нашем словаре такого нет:(')
            

