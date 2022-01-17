
def print_contacts(all_contacts):
    for contact in all_contacts:
        display_one_contact(contact)


def add_new_contact(new_contacts):
    name = input("Enter new name : ")
    surname = input("Enter new surname : ")
    fio = input("Enter new fio : ")
    phone = input("Enter new phone : ")
    country = input("Enter new country : ")
    city = input("Enter new city : ")
    new_contact_dict = {
        "name": name,
        "surname": surname,
        "fio": fio,
        "phone": phone,
        "country": country,
        "city": city,
    }
    new_contacts.append(new_contact_dict)
    print("contact is added")
    print_contacts(new_contacts)


def search_by_name(find_contacts):
    name = input("Enter name that you want to find: ")
    rez = search_any(find_contacts, name, "name")
    print_contacts(rez)


def search_by_surname(find_contacts):
    surname = input("Enter surname that you want to find: ")
    rez = search_any(find_contacts, surname, "surname")
    print_contacts(rez)


def search_by_fio(find_contacts):
    fio = input("Enter fio that you want to find: ")
    rez = search_any(find_contacts, fio, "fio")
    print_contacts(rez)


def search_by_phone(find_contacts):
    phone = input("Enter phone that you want to find: ")
    rez = search_any(find_contacts, phone, "phone")
    print_contacts(rez)


def search_any(find_contacts, q="", field="city"):
    ans = []
    for contact in find_contacts:
        if contact.get(field) == q:
            ans.append(contact)
    return ans


def search_by_city(find_contacts):
    city = input("Enter city that you want to find: ")
    for contact in find_contacts:
        if contact["city"] == city:
            display_one_contact(contact)
    else:
        print("contact with this city is not found ")


def display_one_contact(contact):
    print("{0}, {1}, {2}, {3}, {4}, {5}".format(
        contact["name"],
        contact["surname"],
        contact["fio"],
        contact["phone"],
        contact["country"],
        contact["city"]))