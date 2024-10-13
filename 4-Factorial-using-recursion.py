#Factorial:
def fact(x):
    if x==0:
        return 1
    else:
        return x*fact(x-1)
y=1
x=int(input("enter number:"))
print(fact(x))