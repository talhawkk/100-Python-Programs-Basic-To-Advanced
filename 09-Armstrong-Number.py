#Armstrong Number:

x=int(input("enter number: "))
st=str(x)
len=len(st)
sumofcube=0
for i in st:
    sumofcube+=int(i)**len
if(sumofcube==x):
    print("armstrong")
else:
    print("not")