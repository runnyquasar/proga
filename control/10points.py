lines=[]
with open("/Users/andreakimov/Desktop/freq.txt", encoding="utf-8") as f:
    lines=f.readlines()
 
    for line in lines:
        form=line.split('|')
        user_word=input('Введите слово: ')
        if user_word=='' :
            break
 
        if user_word in lines:
            print(form[1:2])
        else:
            print('takogo net')
            
        
       
        
            

