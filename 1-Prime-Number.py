# Prime number checker
x = int(input("Enter a number: "))
if x > 1:
    for i in range(2, x):
        if x % i == 0:
            print(f"{x} is not a prime number.")
            break
    else:
        print(f"{x} is a prime number.")
else:
    print("Please enter a number greater than 1.")
print(3%3)