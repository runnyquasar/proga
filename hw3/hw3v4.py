x=input("Введите слово: ")

if x != "":
    for letter in x:
        print(x)
        x=x[-1]+x[:-1]
    
