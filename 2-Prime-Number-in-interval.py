#prime number in an interval:

x=int(input("enter lower number : "))
y=int(input("enter higher number : "))
for j in range(x,y):
    if j>1:
        isprime=True
        for i in range(2,j):
            if(j%i==0):
                isprime=False
                break
        if isprime:
            print(j)