def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid input. Usage: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid input. Usage: change [name] [new_phone]"
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    return "Contact not found."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid input. Usage: phone [name]"
    name = args[0]
    return contacts.get(name, "Contact not found.")


def show_all(contacts):
    if not contacts:
        return "No contacts available."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
