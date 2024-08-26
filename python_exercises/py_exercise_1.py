pass
print("what's up?")

# def samp(): 
#     print("The function works!")
#     print("Doesn't it?")

# def stam():
#     pass

# def math(a,b):
#     print(a + b)

# samp()
# math(1,2)

# def bigger(n1,n2):
#     if n1 > n2:
#          print("n1 is bigger")
#     else:
#          print("n2 is bigger")

# def biggerBetter(n1,n2):
#     if n1 > n2: return n1
#     else: return n2

# def twiceString(str):
#     print(str+str)

# res = biggerBetter(40,50)
# # print(res)
# # twiceString("kawabanga")

# ar = [1,4,10]
# arj = [{"model",1234}]

# for immm in ar:
#     print(immm)

# n1 = input("Enter a number:")
# print(f"{n1} * 3 is:{3 * int(n1)}")

import os

os.system('cls' if os.name == 'nt' else 'clear')

# true if condition else false
'cls' if os.name == 'nt' else 'clear'

contacts = []

def getUserData(): 
        name = input("Enter contact name: ")
        email = input("Enter contact email: ")
        contacts.append({"name": name, "email": email})
        print("Contact added.")

def delContact():
        name = input("Enter the name of the contact to delete: ")
        email = input("Enter the email of the contact to delete: ")
        contact_found = False
        for contact in contacts:
            if contact["name"] == name and contact["email"] == email:
                contacts.remove(contact)
                contact_found = True
                print("Contact deleted.")
                break
        if not contact_found:
            print("Contact not found.")

def editContact():
        name = input("Enter the name of the contact to edit: ")
        email = input("Enter the email of the contact to edit: ")
        contact_found = False
        for contact in contacts:
            if contact["name"] == name and contact["email"] == email:
                new_name = input("Enter new name: ")
                new_email = input("Enter new email: ")
                contact["name"] = new_name
                contact["email"] = new_email
                contact_found = True
                print("Contact updated.")
                break
        if not contact_found:
            print("Contact not found.")

def showContacts():
            if contacts:
              print("Contacts:")  
            for contact in contacts:
                print(f"Name: {contact['name']}, Email: {contact['email']}")
            else:
                print("No contacts found.")

def menu():
    print("1 - Add new contact")
    print("2 - Del a contact")
    print("3 - Edit contact")
    print("4 - Show all contacts")
    print("X - Exit")

while True:
    userSelection =  menu()
    if userSelection == "X":exit()

    userSelection = input("Selection? ")
    if userSelection == "X":
        break  # Exit the loop and end the program
    elif userSelection == "1":
        getUserData()
    elif userSelection == "2":
        delContact()
    elif userSelection == "3":
        editContact()
    elif userSelection == "4":
        showContacts()
    else:
        print("Invalid selection. Please try again.")



