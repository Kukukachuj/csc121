# 4/20/2025
#CSC-121
#M6Pro

"""This program is a contact management system that allows users to perform the following operations:

1. Add a new contact with details such as first name, last name, phone number, and email.
2. View all saved contacts in a tabular format.
3. Search for a contact by last name.
4. Remove a contact by specifying the first and last name.
5. Update the phone number of a contact by searching for their last name.
6. Save all contacts to a CSV file and load them when the program starts.

The program ensures data validation for phone numbers and email addresses:
- Phone numbers must follow the format (XXX)XXX-XXXX.
- Email addresses must contain "@" and ".", with exactly three characters after the last ".".

Contacts are stored in a CSV file named `contacts.csv`, and the program handles file operations to persist data between sessions.

Functions:
- `loadContacts()`: Loads contacts from the CSV file.
- `saveContact(contacts)`: Saves the current list of contacts to the CSV file.
- `namesFormat(name)`: Formats names by trimming spaces and capitalizing them.
- `validPhone(phoneNumber)`: Validates the phone number format.
- `validEmail(email)`: Validates the email format.
- `contactAdd(contacts)`: Adds a new contact after validating input.
- `viewContact(contacts)`: Displays all contacts in a tabular format.
- `searchContact(contacts)`: Searches for contacts by last name.
- `removeContact(contacts)`: Removes a contact by first and last name.
- `updateContact(contacts)`: Updates the phone number of a contact.
- `menu()`: Displays the menu, handles user input, and manages the program flow.

"""

import csv


contactDocument = "contacts.csv"


def loadContacts():
    contacts = []
    try:
        with open(contactDocument, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    except Exception:
        print("File not found. Starting fresh with no contacts.")
    return contacts


def saveContact(contacts):
    """
    Writes all contacts to the CSV file.
    """
    with open(contactDocument, "w", newline="") as file:
        fieldnames = ["FirstName", "lastName", "phoneNumber", "email"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)


def namesFormat(name):
    """
    Trims extra spaces and capitalizes the name.
    """
    return name.strip().capitalize()


def validPhone(phoneNumber):
    """
    Validates a phone number.
    Returns True if in form (XXX)XXX-XXXX; otherwise, returns False.
    """
    if len(phoneNumber) != 13:
        return False
    if phoneNumber[0] != "(" or phoneNumber[4] != ")" or phoneNumber[8] != "-":
        return False
    if not (phoneNumber[1:4].isdigit() and phoneNumber[5:8].isdigit() and phoneNumber[9:].isdigit()):
        return False
    return True


def validEmail(email):
    """
    A basic email checker that validates the presence of '@' and '.'.
    It also checks that exactly three characters follow the last '.'.
    """
    if "@" in email and "." in email:
        last_dot = email.rfind(".")
        if len(email) - last_dot - 1 == 3:
            return True
    return False


def contactAdd(contacts):
    """
    Prompts the user to add a new contact.
    If the phone or email format is wrong, no contact is added.
    """
    first = namesFormat(input("Enter First name: "))
    last = namesFormat(input("Enter Last name: "))
    phoneNumber = input("Phone ((XXX)XXX-XXXX): ")
    email = input("Email: ")

    if not validPhone(phoneNumber):
        print("Phone format is wrong. Contact not added!")
        return
    if not validEmail(email):
        print("Email format is not valid. Contact not added!")
        return

    contact = {
        "FirstName": first,
        "lastName": last,
        "phoneNumber": phoneNumber,
        "email": email,
    }
    contacts.append(contact)
    print("Contact has been added!")


def viewContact(contacts):
    """
    Prints all contacts in a simple table format.
    """
    print("\nContacts:")
    print("FirstName\tLastName\tPhone\t\tEmail")
    print("----------------------------------------------")
    for c in contacts:
        # Use tab characters to separate fields for simplicity.
        print(f"{c['FirstName']}\t{c['lastName']}\t{c['phoneNumber']}\t{c['email']}")
    print()


def searchContact(contacts):
    """
    Searches for contacts by last name.
    Displays matching contacts if found.
    """
    search = input("Enter last name to search: ").lower()
    found = False
    for c in contacts:
        if c["lastName"].lower() == search:
            print(c)
            found = True
    if not found:
        print("No contact found with that last name.")


def removeContact(contacts):
    """
    Removes a contact that matches the given first and last name.
    """
    first = namesFormat(input("Enter First name to remove: "))
    last = namesFormat(input("Enter Last name to remove: "))
    removed = False
    for c in contacts:
        if c["FirstName"] == first and c["lastName"] == last:
            contacts.remove(c)
            print("Contact removed successfully!")
            removed = True
            break
    if not removed:
        print("No matching contact was found.")


def updateContact(contacts):
    """
    Updates a contact's phone number.
    The function searches for contacts by last name.
    If one contact is found, it updates immediately.
    If multiple are found, the user is prompted to choose which one to update.
    """
    last = namesFormat(input("Enter last name to update: "))
    found = []
    for c in contacts:
        if c["lastName"] == last:
            found.append(c)

    if len(found) == 0:
        print("No contact found with that last name.")
    elif len(found) == 1:
        new_phone = input("New phone number ((XXX)XXX-XXXX): ")
        if validPhone(new_phone):
            found[0]["phoneNumber"] = new_phone
            print("Phone number updated.")
        else:
            print("Bad phone number format.")
    else:
        print("Multiple contacts found:")
        for i, contact in enumerate(found):
            print(f"{i+1}: {contact}")
        choice = input("Which one to update? (enter number): ")
        if choice.isdigit():
            num = int(choice) - 1
            if 0 <= num < len(found):
                new_phone = input("New phone number ((XXX)XXX-XXXX): ")
                if validPhone(new_phone):
                    found[num]["phoneNumber"] = new_phone
                    print("Phone number updated.")
                else:
                    print("Bad phone number format.")
            else:
                print("Invalid choice number.")
        else:
            print("You did not enter a valid number.")


def menu():
    """
    Displays the menu and handles user input.
    The contact list is loaded at the beginning and saved when exiting.
    """
    contacts = loadContacts()
    while True:
        print("\n--- MENU ---")
        print("1) Add Contact")
        print("2) View Contacts")
        print("3) Search Contact")
        print("4) Remove Contact")
        print("5) Update Contact")
        print("6) Exit")
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            contactAdd(contacts)
        elif choice == "2":
            viewContact(contacts)
        elif choice == "3":
            searchContact(contacts)
        elif choice == "4":
            removeContact(contacts)
        elif choice == "5":
            updateContact(contacts)
        elif choice == "6":
            saveContact(contacts)
            print("Saving contacts and exiting program...")
            break
        else:
            print("Invalid option. Please try again.")


# Start the program
menu()
