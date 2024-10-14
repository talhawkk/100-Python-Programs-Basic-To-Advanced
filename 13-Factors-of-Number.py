#find factors of a number:
x=int(input("enter numbers : "))
for i in range(1,x+1):
    if (x%i==0):
        print(i)