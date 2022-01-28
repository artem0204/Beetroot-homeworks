from task1.task1 import contacts
from task1.task1 import print_contacts
from task1.task1 import add_new_contact
from task1.task1 import search_by_name
from task1.task1 import search_by_fio
from task1.task1 import search_by_city
from task1.task1 import search_by_surname
from task1.task1 import search_by_phone

import task2.task2

if __name__ == '__main__':
    print_contacts(contacts)
    add_new_contact(contacts)
    search_by_name(contacts)
    search_by_surname(contacts)
    search_by_fio(contacts)
    search_by_phone(contacts)
    search_by_city(contacts)