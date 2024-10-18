# finding leap year:

x = int(input("Enter year: "))
if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
