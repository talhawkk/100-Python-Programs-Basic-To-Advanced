#decimal to binary using recursion fucntion:
def binary(num):
    if num>1:
        binary(num//2)
    print(num%2)
num=int(input("enter number "))
binary(num)