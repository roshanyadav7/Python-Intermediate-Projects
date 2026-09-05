import json

contacts = []

# =========================
# FILE HANDLING
# =========================

def load_contacts():
    global contacts

    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)

    except FileNotFoundError:
        contacts = []

    except json.JSONDecodeError:
        print("Warning: contacts.json contains invalid data.")
        contacts = []


def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)


# =========================
# INPUT VALIDATION
# =========================

def get_name(prompt):
    while True:
        name = input(prompt).strip()

        if not name:
            print("Name cannot be empty.")
            continue

        if not all(char.isalpha() or char.isspace() for char in name):
            print("Name can contain only letters and spaces.")
            continue

        return name


def get_phone(prompt):
    while True:
        phone = input(prompt).strip()

        if not phone:
            print("Phone number cannot be empty.")
            continue

        if not phone.isdigit():
            print("Phone number must contain only digits.")
            continue

        if len(phone) != 10:
            print("Phone number must contain exactly 10 digits.")
            continue

        return phone


def get_email(prompt):
    while True:
        email = input(prompt).strip()

        if not email:
            print("Email cannot be empty.")
            continue

        if "@" not in email or "." not in email.split("@")[-1]:
            print("Please enter a valid email address.")
            continue

        return email


# =========================
# DUPLICATE CHECK
# =========================

def phone_exists(phone):
    for contact in contacts:
        if contact["phone"] == phone:
            return True

    return False


# =========================
# ADD CONTACT
# =========================

def add_contact():
    print("\n--- Add Contact ---")

    name = get_name("Enter name: ")

    while True:
        phone = get_phone("Enter phone: ")

        if phone_exists(phone):
            print("A contact with this phone number already exists.")
        else:
            break

    email = get_email("Enter email: ")
    address = input("Enter address: ").strip()

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    save_contacts()

    print("\nContact added successfully!")


# =========================
# VIEW CONTACTS
# =========================

def view_contacts():
    print("\n--- Contacts ---")

    if not contacts:
        print("No contacts found.")
        return

    for index, contact in enumerate(contacts, start=1):
        print(f"\nContact {index}")
        print("-" * 30)
        print(f"Name    : {contact['name']}")
        print(f"Phone   : {contact['phone']}")
        print(f"Email   : {contact['email']}")
        print(f"Address : {contact['address']}")


# =========================
# SEARCH CONTACT
# =========================

def search_contacts():
    print("\n--- Search Contact ---")

    if not contacts:
        print("No contacts available.")
        return

    search = input("Enter name or phone number: ").strip().lower()

    if not search:
        print("Search cannot be empty.")
        return

    found = False

    for contact in contacts:
        if (
            search in contact["name"].lower()
            or search in contact["phone"]
        ):
            print("\nContact Found")
            print("-" * 30)
            print(f"Name    : {contact['name']}")
            print(f"Phone   : {contact['phone']}")
            print(f"Email   : {contact['email']}")
            print(f"Address : {contact['address']}")

            found = True

    if not found:
        print("\nNo matching contact found.")


# =========================
# UPDATE CONTACT
# =========================

def update_contact():
    print("\n--- Update Contact ---")

    if not contacts:
        print("No contacts available.")
        return

    name = input(
        "Enter the name of the contact to update: "
    ).strip().lower()

    if not name:
        print("Name cannot be empty.")
        return

    for contact in contacts:

        if contact["name"].lower() == name:

            print("\nContact Found")
            print("-" * 30)
            print(f"Name    : {contact['name']}")
            print(f"Phone   : {contact['phone']}")
            print(f"Email   : {contact['email']}")
            print(f"Address : {contact['address']}")

            print("\nEnter new information.")
            print("Press Enter to keep the existing value.")

            # -------------------------
            # UPDATE NAME
            # -------------------------

            new_name = input(
                f"Name [{contact['name']}]: "
            ).strip()

            if new_name:

                if all(
                    char.isalpha() or char.isspace()
                    for char in new_name
                ):
                    contact["name"] = new_name
                else:
                    print(
                        "Invalid name. Keeping the old name."
                    )

            # -------------------------
            # UPDATE PHONE
            # -------------------------

            new_phone = input(
                f"Phone [{contact['phone']}]: "
            ).strip()

            if new_phone:

                if not new_phone.isdigit():
                    print(
                        "Phone must contain only digits. "
                        "Keeping the old phone."
                    )

                elif len(new_phone) != 10:
                    print(
                        "Phone must contain exactly 10 digits. "
                        "Keeping the old phone."
                    )

                elif (
                    new_phone != contact["phone"]
                    and phone_exists(new_phone)
                ):
                    print(
                        "This phone number already belongs "
                        "to another contact."
                    )

                else:
                    contact["phone"] = new_phone

            # -------------------------
            # UPDATE EMAIL
            # -------------------------

            new_email = input(
                f"Email [{contact['email']}]: "
            ).strip()

            if new_email:

                if (
                    "@" in new_email
                    and "." in new_email.split("@")[-1]
                ):
                    contact["email"] = new_email
                else:
                    print(
                        "Invalid email. "
                        "Keeping the old email."
                    )

            # -------------------------
            # UPDATE ADDRESS
            # -------------------------

            new_address = input(
                f"Address [{contact['address']}]: "
            ).strip()

            if new_address:
                contact["address"] = new_address

            save_contacts()

            print("\nContact updated successfully!")
            return

    print("\nContact not found.")


# =========================
# DELETE CONTACT
# =========================

def delete_contact():
    print("\n--- Delete Contact ---")

    if not contacts:
        print("No contacts available.")
        return

    name = input(
        "Enter the name of the contact to delete: "
    ).strip().lower()

    if not name:
        print("Name cannot be empty.")
        return

    for contact in contacts:

        if contact["name"].lower() == name:

            print("\nContact Found")
            print("-" * 30)
            print(f"Name    : {contact['name']}")
            print(f"Phone   : {contact['phone']}")
            print(f"Email   : {contact['email']}")
            print(f"Address : {contact['address']}")

            confirm = input(
                "\nAre you sure you want to delete "
                "this contact? (y/n): "
            ).strip().lower()

            if confirm == "y":

                contacts.remove(contact)
                save_contacts()

                print("\nContact deleted successfully!")

            else:
                print("\nDeletion cancelled.")

            return

    print("\nContact not found.")


# =========================
# MAIN PROGRAM
# =========================

load_contacts()

print("=" * 50)
print("                CONTACT BOOK")
print("=" * 50)

while True:

    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contacts()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 6.")