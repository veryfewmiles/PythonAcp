import sys
def create_phonebook():
    rows = int(input("Enter number of contacts: "))
    phonebook = []
    for i in range(rows):
        print("\nEnter contact", i + 1)
        name = input("Enter name: ")
        number = int(input("Enter number: "))
        email = input("Enter email: ")
        dob = input("Enter DOB: ")
        category = input("Enter category: ")
        if name == "" or name == " ":
            sys.exit("Name cannot be empty")
        phonebook.append([name, number, email, dob, category])
    return phonebook
def menu():
    print("\n--- PHONEBOOK ---")
    print("1. Add contact")
    print("2. Remove contact")
    print("3. Delete all")
    print("4. Search")
    print("5. Show contacts")
    print("6. Exit")
    choice = int(input("Enter choice: "))
    return choice
def add_contact(pb):
    contact = []
    contact.append(input("Enter name: "))
    contact.append(int(input("Enter number: ")))
    contact.append(input("Enter email: "))
    contact.append(input("Enter DOB: "))
    contact.append(input("Enter category: "))
    pb.append(contact)
    return pb
def remove_contact(pb):
    name = input("Enter contact name: ")
    found = False
    for i in range(len(pb)):
        if pb[i][0] == name:
            print(pb.pop(i))
            print("Contact removed")
            found = True
            break
    if found == False:
        print("Contact not found")
    return pb
def search_contact(pb):
    name = input("Enter name to search: ")
    found = []
    for contact in pb:
        if contact[0] == name:
            found.append(contact)
    if len(found) == 0:
        print("Contact not found")
    else:
        for contact in found:
            print(contact)
def show_contacts(pb):
    if not pb:
        print("Phonebook is empty")
    else:
        for i in range(len(pb)):
            print(pb[i])
print("****************************")
print("Welcome to my Phonebook")
print("****************************")
pb = create_phonebook()
ch = 0
while ch != 6:
    ch = menu()
    if ch == 1:
        pb = add_contact(pb)
    elif ch == 2:
        pb = remove_contact(pb)
    elif ch == 3:
        pb.clear()
        print("All contacts deleted")
    elif ch == 4:
        search_contact(pb)
    elif ch == 5:
        show_contacts(pb)
    elif ch == 6:
        print("Goodbye!")
    else:
        print("Invalid choice")