def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please"
        except KeyError:
            return "Contact not found"
        except IndexError:
            return "Invalid input. Please provide the correct contact data"

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error  # Decorator added
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added"


@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated"
    raise KeyError


@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise ValueError
    name = args[0]
    return contacts.get(name, "Sorry, contact not found")


@input_error
def show_all(contacts):
    if not contacts:
        return "Sorry, no contacts found"
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
