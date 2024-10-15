#Palindrome
x=str(input("enter String to check : "))
# l=len(x)
# if x[0]==x[l-1] and x[1]==x[l-2] and x[2]==x[l-3]:
#     print("palindrome")
# else:
#     print("not")
rev=x[::-1]
if x==rev:
    print("palindrome")
else:
    print("not")