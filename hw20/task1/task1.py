contacts = [
    {"name": "artem",
     "surname": "podgorniy",
     "fio": "artem podgorniy",
     "phone": "0957187572",
     "country": "Ukraine",
     "city": "Kyiv"},
    {"name": "mykola",
     "surname": "steblinsky",
     "fio": "mykola steblinsky",
     "phone": "0979541273",
     "country": "Germany",
     "city": "Berlin"},
    {"name": "Nastya",
     "surname": "Gavrilova",
     "fio": "Nastya Gavrilova",
     "phone": "0954087581",
     "country": "Norven",
     "city": "bangladeh"},
]


def print_contacts(all_contacts: list)-> None:
    for contact in all_contacts:
        display_one_contact(contact)


def add_new_contact(new_contacts: list)-> None:
    name: str = input("Enter new name : ")
    surname: str = input("Enter new surname : ")
    fio: str = input("Enter new fio : ")
    phone: str = input("Enter new phone : ")
    country: str = input("Enter new country : ")
    city: str = input("Enter new city : ")
    new_contact_dict: dict = {
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


def search_by_name(find_contacts: list)-> None:
    name: str = input("Enter name that you want to find: ")
    rez = search_any(find_contacts, name, "name")
    print_contacts(rez)


def search_by_surname(find_contacts: list)-> None:
    surname: str = input("Enter surname that you want to find: ")
    rez = search_any(find_contacts, surname, "surname")
    print_contacts(rez)


def search_by_fio(find_contacts: list)-> None:
    fio: str = input("Enter fio that you want to find: ")
    rez = search_any(find_contacts, fio, "fio")
    print_contacts(rez)


def search_by_phone(find_contacts: list) -> None:
    phone: str = input("Enter phone that you want to find: ")
    rez = search_any(find_contacts, phone, "phone")
    print_contacts(rez)


def search_any(find_contacts: list, q: str = "", field: str = "city") -> list:
    ans: list = []
    for contact in find_contacts:
        if contact.get(field) == q:
            ans.append(contact)
    return ans


def search_by_city(find_contacts: list) -> None:
    city: str = input("Enter city that you want to find: ")
    for contact in find_contacts:
        if contact["city"] == city:
            display_one_contact(contact)
    else:
        print("contact with this city is not found ")


def display_one_contact(contact: dict) -> None:
    print("{0}, {1}, {2}, {3}, {4}, {5}".format(
        contact["name"],
        contact["surname"],
        contact["fio"],
        contact["phone"],
        contact["country"],
        contact["city"]))


