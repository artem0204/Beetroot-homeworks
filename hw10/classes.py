# task 1
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def display_person(self):
        print(f"name :{self.name}, surname: {self.surname}, age: {self.age}")


class Student(Person):
    subjects = []
    grade = []

    def display_student(self):
        print(
            f"name: {self.name}, surname: {self.surname}, age: {self.age},subject: {self.subjects}, grade : {self.grade}")


class Teacher(Person):
    salary = 10000
    position = "laborant"

    def display_Teacher(self):
        print(
            f" name:{self.name}, surname: {self.surname}, age: {self.age}, salary: {self.salary}, position: {self.position}")


# task 2
class Mathematician:
    def square_nums(self, listNums):
        rez = []
        for i in listNums:
            rez.append(i ** 2)
        return rez

    def remove_positives(self, ListNums):
        rez = []
        for i in ListNums:
            if i < 0:
                rez.append(i)
        return rez

    def filter_leaps(self, ListLeaps):
        rez = []
        for i in ListLeaps:
            if i % 4 == 0:
                rez.append(i)
        return rez


# task
# 3


class Product:
    def __init__(self, type, title, price):
        self.type = type
        self.title = title
        self.price = price
        self.amount = 0

    def display_product(self):
        print(f"type: {self.type}, title: {self.title}, price: {self.price} amount: {self.amount}")


class ProductStore:
    def __init__(self):
        self.listOfProduct = []
        self.priceForStore = 30

    def add(self,product, amount, ):
        if amount <= 0:
            raise ValueError("Canot add negative amount of product")
        else:
            product.price *= 1 + (30 / 100)
            product.amount = amount
            self.listOfProduct.append(product.display_product())
        return self.listOfProduct
    """Остальное не смог разобрать ( """





# task 4
class CustomExeption(Exception):
    def __init__(self, msg, message="dont use upper case"):
        self.msg = msg
        self.message = message
        super().__init__(self.message)
