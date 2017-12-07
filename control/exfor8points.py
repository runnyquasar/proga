lines=[]
with open("/Users/andreakimov/Desktop/freq.txt", encoding="utf-8") as f:
    lines=f.readlines()
    ipm=0
    for line in lines:        
        form=line.split('|')        
        if form[1]==' част ':
            print(form[:1],',',end=' ')
            ipm+=float(form[2])
    print(ipm)
 
            
            
                
    
 
                









