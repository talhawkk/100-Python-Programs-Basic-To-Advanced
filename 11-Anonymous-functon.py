
#Display Powers of 2 Using Anonymous Function:

terms=int(input("enter number of terms : "))
result=list(map(lambda x : 2**x, range(1,terms+1)))
print(result)