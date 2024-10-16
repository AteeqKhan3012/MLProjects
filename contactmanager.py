contacts = {}  # empty dictionary

def add_contact(name, phone_number, email):
    """Add a new contact"""
    if not name or not phone_number or not email:
        raise ValueError("All fields are required")
    contacts[name] = {"phone_number": phone_number, "email": email}

def search_contact(name):
    """Search for a contact by name"""
    return contacts.get(name)

def update_contact(name, phone_number=None, email=None):
    """Update a contact's details"""
    if name not in contacts:
        raise ValueError("Contact not found")
    if phone_number:
        contacts[name]["phone_number"] = phone_number
    if email:
        contacts[name]["email"] = email

def display_contacts():
    """Display all contacts"""
    for name, details in contacts.items():
        print(f"Name: {name}")
        print(f"Phone Number: {details['phone_number']}")
        print(f"Email: {details['email']}")

def filter_contacts(email_domain):
    """Filter contacts by email domain"""
    return [contact for contact in contacts.values() if contact["email"].endswith(email_domain)]

def contact_manager():
    while True:
        print("\n Contact Manager ")
        print("\n 1. Add your Contact ")
        print("\n 2. Search your contact ")
        print("\n 3. Update your contact here ")
        print("\n 4. Display all contacts ")
        print("\n 5. Filter the contacts with email acc of your choice ")
        print("\n 6. Quit the program ")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter your email: ")
            try:
                add_contact(name, phone_number, email)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            name = input("Enter name: ")
            contact = search_contact(name)
            if contact:
                print(f"Phone Number: {contact['phone_number']}")
                print(f"Email: {contact['email']}")
            else:
                print("Sorry! Contact not found.")
        elif choice == "3":
            name = input("Enter name: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            try:
                update_contact(name, phone_number, email)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "4":
            display_contacts()
        elif choice == "5":
            email_domain = input("Enter email domain: ")
            filtered_contacts = filter_contacts(email_domain)
            for contact in filtered_contacts:
                print(f"Name: {contact['name']}")
                print(f"Phone Number: {contact['phone_number']}")
                print(f"Email: {contact['email']}")
        elif choice == "6":
            break
        else:
            print("Oops! It's invalid. Please choose again.")

contact_manager()