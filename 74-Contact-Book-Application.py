import json



while True:
    print("\n***********Contack Book**********")
    choice = int(input("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Exit\nChoose an option: "))
    if choice==1:
        add()
    elif choice==2:
        view()
    elif choice==3:
        search()
    elif choice==4:
        break
    else:
        print("Invalid Option")