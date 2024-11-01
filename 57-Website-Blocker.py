def blocker(path1, redirect1, site1):
    with open(path1, 'r+') as f:
        contain = f.read()
        if site1 not in contain:
            f.write(redirect1 + " " + site1 + "\n")  # Corrected to use site1
    print("Blocked")

def unblocker(path1, site1):
    with open(path1, 'r') as f:
        lines = f.readlines()
    with open(path1, 'w') as f:
        for line in lines:
            if site1 not in line:
                f.write(line)
    print("Unblocked")

path = "C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"
site = input("Enter the URL of the website that you want to block or unblock: ")
c = int(input("Enter 1 if you want to block the website or enter 2 if you want to unblock the website: "))
if c == 1:
    blocker(path, redirect, site)
elif c == 2:
    unblocker(path, site)

