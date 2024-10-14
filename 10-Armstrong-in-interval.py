#Armstrong number in an interval:
lower=int(input("enter lower number: "))
higher=int(input("enter highr value : "))
for i in range(lower,higher):
    st=str(i)
    n=len(st)
    sumof=0
    for j in st:
        sumof+=int(j)**n
    if(i==sumof):
        print(i)