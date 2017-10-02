x=int(input("Enter x:"))
y=int(input("Enter y:"))
z=int(input("Enter z:"))

if x+y==z:
    if x/y==z:
        print("how is it possible?")
    else:
        print("x+y=z, but x/y!=z")
else:
    if x/y==z:
        print("x/y=z, but x+y!=z")
    else:
        print("nothing works")
    

print("The end")
