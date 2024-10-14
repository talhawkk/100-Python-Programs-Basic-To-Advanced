#print natural number using recursion:
def sum(x):
    if x<=1:
        return x
    else:
        return x+sum(x-1)
x=int(input("enter number : "))
print(sum(x))