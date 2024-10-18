n=str(input("enter your code word:\n"))
s,e,n2,n3="ast","tsa","",""
if len(n)==3 or len(n)>3:
    n1=n[1:]
    n2=s + n1 + n[0] + e
else:
    for char in n[::-1]:
        n2+=char
print(n2)
print("\n\n DECODING:\n")
if len(n)<3:
    for char in n2[::-1]:
        n3+=char
else:
    n1 = n2[3:-3]
    n3 = n1[-1] + n1[:-1]
print(n3)