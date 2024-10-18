#check if a string is a reserved keyword in python :
import keyword
l=[]
for i in range (6):
    x=str(input("enter word : "))
    l.append(x)
for i in l:
    if keyword.iskeyword(i):
        print(f"{i} is a python reserved keyword, you can not use this as variable, method name")
    else:
        print(f"{i} is not keyword")