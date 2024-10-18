# #Fibanocci sequence:
a,b=0,1
num=int(input("enter number : "))
if num==1:
    print(0)
else:
    print(a,"\n",b,sep="")
    for i in range(2,num):
        
        c=a+b
        a=b
        b=c
        print(c)