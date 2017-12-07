freq=[]
with open("/Users/andreakimov/Desktop/freq.txt", encoding="utf-8") as f:
    lines=f.readlines()
    for line in lines:
        if 'перех' in line:
            print(line)
            form=line.split(' ')
            
        
        
    
    
