class Animal:
    def talk(self):
        print("Animals can talk")


class Dog(Animal):
    def __talk__(self):
        print("woof woof")


class Cat(Animal):
    def __talk__(self):
        print("meow meow")


class Fraction:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        return self.value / other.value

    def __eq__(self, other):
        return self.value == other.value


# task 2
class Library:
    def __init__(self, name):
       self.name = name
       self.books= []
       self.authors = []
    def new_book(self,name,year,author):
        book = Book(name,year,author)
        self.books.append(book)
        self.authors.append(author)
        return book
    def group_by_author(self,author):
        author_list = []
        for book in self.books:
            if author in self.authors:
                author_list.append(book)
        return author_list
    def group_by_year(self,year):
        year_list = []
        for book in self.books:
            if year == book.year:
                year_list.append(book)
        return year_list

    def __repr__(self):
        return f"Для {self.name}, есть книги: {self.books}. "


class Book:
    amount_of_books = 0

    def __init__(self,name,year,author):
        self.name = name
        self.year = year
        self.author = author
        self.amount_of_books += 1
    def __repr__(self):
        return f"{self.name}, книга {self.year} год выпуска, {self.author}"


class Author:
    def __init__(self,name,country,birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []
    def  __repr__(self):
        return f"Автор: {self.name}, из {self.country}, родился {self.birthday}"

