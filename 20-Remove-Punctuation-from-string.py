#Remove punctuation from strings:
n=str(input("enter string : "))
P='''!@#$%^&*()-;:\|,'".<>?'''
st=""
for i in n:
    if i  not in P:
        st+=i
print(st)