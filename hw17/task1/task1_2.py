def display_one_contact(contact):
    print("{0}, {1}, {2}, {3}, {4}, {5}".format(
        contact["name"],
        contact["surname"],
        contact["fio"],
        contact["phone"],
        contact["country"],
        contact["city"]))