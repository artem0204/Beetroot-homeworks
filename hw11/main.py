from classes import Dog, Cat, Fraction, Library, Book, Author


def talk_test(obj):
    obj.__talk__()


if __name__ == '__main__':
    dog = Dog()
    cat = Cat()
    talk_test(dog)
    talk_test(cat)

# task2
library1 = Library("Городская библиотека")
library2 = Library("Центральная библиотека")
author1 = Author("Достоевский", "Россия", 1821)
author2 = Author("Шевченко", "Украина", 1814)
author3 = Author("Шевченко", "Украина", 1856)
book1 = Book("Преступление и наказание", 1866, "Достоевский")
book2 = Book("Кобзаря", 1840, "Шевченко")
book3 = Book("Захар Беркут", 1840, "Шевченко")
print(library1.new_book(book1, 1866, author1))
print(library2.new_book(book2, 1840, author2))
print(library2.new_book(book3, 1883, author3))
print(library2.group_by_author(author3))
print(library2.group_by_year(1840))
# task 3

x = Fraction(1 / 2)
y = Fraction(1 / 4)
print(x + y, x - y, x * y, x / y)
assert Fraction(x + y) == Fraction(3 / 4)
