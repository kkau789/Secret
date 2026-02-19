import os

PIN = "1234"
FILE = "secrets.txt"

def clear():
    os.system("clear")

def login():
    for i in range(3):
        pin = input("Enter PIN: ")
        if pin == PIN:
            return True
        else:
            print("Wrong PIN")
    return False

def menu():
    while True:
        print("\n--- Secret Vault ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            note = input("Write secret note: ")
            with open(FILE, "a") as f:
                f.write(note + "\n")
            print("Saved 🔐")

        elif choice == "2":
            if os.path.exists(FILE):
                with open(FILE, "r") as f:
                    print("\nYour Secrets:")
                    print(f.read())
            else:
                print("No secrets yet.")

        elif choice == "3":
            break

        else:
            print("Invalid option")

clear()

if login():
    menu()
else:
    print("Access denied.")
