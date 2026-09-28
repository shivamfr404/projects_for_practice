print(r"""
███████╗██╗  ██╗██╗██╗   ██╗ █████╗ ███╗   ███╗
██╔════╝██║  ██║██║██║   ██║██╔══██╗████╗ ████║
███████╗███████║██║██║   ██║███████║██╔████╔██║
╚════██║██╔══██║██║╚██╗ ██╔╝██╔══██║██║╚██╔╝██║
███████║██║  ██║██║ ╚████╔╝ ██║  ██║██║ ╚═╝ ██║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═╝  ╚═╝╚═╝     ╚═╝
""")

print("=" * 60)
print("                PASSWORD MANAGER")
print("                 Created by SHIVAM")
print("      A fun project built for learning Python.")
print("=" * 60)

ask = input("\nChoose an option (view/add/quit): ").lower()


def view():
    try:
        with open("password.txt", "r") as f:
            print("\nSaved Passwords")
            print("-" * 60)

            for line in f:
                print(line.strip())

    except FileNotFoundError:
        print("\nNo saved passwords found.")


def add():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("password.txt", "a") as f:
        f.write(username + " | " + password + "\n")

    print("\n✓ Password added successfully!")


while True:
    if ask == "view":
        view()
        break

    elif ask == "add":
        add()
        break

    elif ask == "quit":
        print("\nThank you for using Password Manager.")
        print("Goodbye!")
        break

    else:
        print("\n❌ Invalid option.")
        print("Please enter: view, add, or quit.")

    ask = input("\nChoose an option (view/add/quit): ").lower()