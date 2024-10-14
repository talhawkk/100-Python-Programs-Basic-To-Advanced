#fiboncci sequence:
try:
    def fi(x):
        if x<=1:
            return x
        else:
            return fi(x-1)+fi(x-2)
    x=int(input("enter a positive number : "))

    for i in range(x):
        print(fi(i))
except Exception as a:
    print("error occur : ",a)