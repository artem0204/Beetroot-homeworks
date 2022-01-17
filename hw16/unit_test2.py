import unittest
import phonebook


class TestPhoneBook(unittest.TestCase):
    def setUp(self):
        self.contacts = [
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

    def test_print_contacts(self):
        for contact in self.contacts:
            rez = phonebook.display_one_contact(contact)
        self.assertEqual(phonebook.print_contacts(self.contacts),rez)

