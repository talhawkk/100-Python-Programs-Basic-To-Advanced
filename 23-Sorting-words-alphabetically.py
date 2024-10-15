#Sorting words in alphabetically order
x=input("enter your string: ")
y=x.split(" ")
# print(y)
for i in range(len(y)):
    y[i]=y[i].lower()
y.sort()
sorted=' '.join(y)
print(sorted)
# print(type(sorted))
# print(type(y))
