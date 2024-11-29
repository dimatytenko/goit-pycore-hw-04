def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Invalid number of arguments."

def change_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact updated."
    except ValueError:
        return "Invalid number of arguments."

def show_phone(args, contacts):
    try:
        name = args[0]
        return contacts[name]
    except KeyError:
        return "Contact not found."
    except ValueError:
        return "Invalid number of arguments."
    except IndexError:
        return "Invalid number of arguments."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(contacts)
        elif command == "help":
            print("Available commands: hello, add, change, phone, all, help, close or exit")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
