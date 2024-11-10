import json



def add():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts = load()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully!")

def save_contacts(contacts):
     with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def load():
    try:
        with open("contacts.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def view():
    contacts=load()
    if not contacts:
        print("not contacts found")
    else:
        for contact in contacts:
            print(contact)


def search():
    search_name=input("enter name to search : ")
    contacts=load()
    for contact in contacts:
        if contact["name"].lower()==search_name.lower():
            print(contact)
            return
    print("contact not found")


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