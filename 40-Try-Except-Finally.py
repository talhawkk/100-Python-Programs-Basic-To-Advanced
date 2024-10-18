def aa():
    try:
        x=int(input("enter your age : "))
        print(x)
        # print(f"your age is {x}")
        return x
    except Exception as e:
        print("error occured : ",e)
        return 0
    finally:
        print("exception handling")
    

yas=aa()
print(yas)