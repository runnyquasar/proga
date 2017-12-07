lines=[]
with open("/Users/andreakimov/Desktop/freq.txt", encoding="utf-8") as f:
    lines=f.readlines()
    c=0
    for line in lines:
        
        form=line.split('|')
        
        if form[1]==' част ':
            print(form[:1],',')
            c+=float(form[2])
    print(c)
 
            
            
                
    
 
                









