lines=[]
with open("/Users/andreakimov/Desktop/freq.txt", encoding="utf-8") as f:
    lines=f.readlines()
    for line in lines:
        form=line.split('|')
        if form[1]==' част ':
            print(form[:1],',')
            ipm=line[-1]
            ipm.strip('\n')
            print(sum(ipm))
 
                









#user_country=input('your country: ')
#found_answer=False
#for line in lines2016[:15]:
#    if line[0] == user_country:
#        value= float(line[3].strip())
#        print(value)
#        break
#    if not found_answer:
#        print('sorry')
#bl=[cells[3],cells[0]]
#sorted(bl, reverse=True)
