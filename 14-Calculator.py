#calculator with match statement:
a=str(input("enter operator one of operator (+,-,/,*) : "))
x=float(input("enter value for x : "))
y=float(input("enter enete value for y : "))

match a:
    case "+":
        print(x+y)
    case "-":
        print(x-y)
    case "%":
        print(x%y)
    case "/":
        print(x/y)
    case "*":
        print(x*y)
    case _:
        print("enter correct operator ")