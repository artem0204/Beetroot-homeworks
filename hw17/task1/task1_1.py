from task1.task1_2 import display_one_contact

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



def print_contacts(all_contacts):
    for contact in all_contacts:
        display_one_contact(contact)

print_contacts(contacts)
