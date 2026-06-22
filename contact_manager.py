import json
import os

CONTACTS_FILE = "contacts.json"


def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return {}
    with open(CONTACTS_FILE, "r") as file:
        return json.load(file)


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter Name: ").strip()
    if not name:
        print("❌ Name cannot be empty.")
        return

    if name.lower() in [n.lower() for n in contacts]:
        print(f"⚠️  Contact '{name}' already exists.")
        return

    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    save_contacts(contacts)
    print(f"✅ Contact '{name}' added successfully.")


def search_contact(contacts):
    query = input("Enter name or phone to search: ").strip().lower()

    results = []
    for name, details in contacts.items():
        if query in name.lower() or query in details["phone"] or query in details["email"].lower():
            results.append((name, details))

    if not results:
        print("⚠️  No contacts found.")
        return

    print(f"\n🔍 Found {len(results)} result(s):")
    print("-" * 35)
    for name, details in results:
        print(f"Name  : {name}")
        print(f"Phone : {details['phone']}")
        print(f"Email : {details['email']}")
        print("-" * 35)


def display_all_contacts(contacts):
    if not contacts:
        print("⚠️  No contacts saved yet.")
        return

    print(f"\n📋 All Contacts ({len(contacts)} total)")
    print("=" * 35)
    for name, details in contacts.items():
        print(f"Name  : {name}")
        print(f"Phone : {details['phone']}")
        print(f"Email : {details['email']}")
        print("-" * 35)


def main():
    contacts = load_contacts()
    print("📱 Contact Management System")

    while True:
        print("\n===== MENU =====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. View All Contacts")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            display_all_contacts(contacts)
        elif choice == "4":
            print("✅ Goodbye!")
            break
        else:
            print("❌ Invalid choice! Enter 1-4.")


if __name__ == "__main__":
    main()
  
