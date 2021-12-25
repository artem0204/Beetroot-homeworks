import re
from functools import wraps


class Validate():
    def __init__(self, email: str):
        self.email = email

    @classmethod
    def validate(cls, email: str):
        rez = "^[a-z0-9]+[\._-]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if not re.search(rez, email):
            print("wrong email name ")
        else:
            print(f"we got your email - {email}")
            return email


# task2

class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers_ = []

    def __repr__(self):
        return f"boss: {self.name}, workers: {self.workers_}"


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss
        self.boss.workers_.append(self)

    @property
    def get_boss(self):
        return self.boss

    @get_boss.setter
    def get_boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self.boss.workers_.remove(self)
            self.boss = new_boss
            self.boss.workers_.append(self)

    def __repr__(self):
        return f"{self.id} - {self.name}, company:{self.company}"

# task3
class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def convert_to_int(*args,**kwargs):
            print("converted to int ")
            try:
                rez = func(*args,**kwargs)
                return int(rez)
            except TypeError:
                print("somthing wrong")
        return convert_to_int

    @staticmethod
    def to_str(func):
        @wraps(func)
        def convert_to_str(*args,**kwargs):
            print("converted to str ")
            try:
                rez = func(*args,**kwargs)
                return str(rez)
            except TypeError:
                print("somthing wrong")
        return convert_to_str

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def convert_to_bool(*args, **kwargs):
            print("converted to bool ")
            try:
                rez = func(*args, **kwargs)
                return bool(rez)
            except TypeError:
                print("somthing wrong")

        return convert_to_bool

    @staticmethod
    def to_float(func):
        @wraps(func)
        def convert_to_float(*args, **kwargs):
            print("converted to float ")
            try:
                rez = func(*args, **kwargs)
                return float(rez)
            except TypeError:
                print("somthing wrong")

        return convert_to_float






if __name__ == '__main__':
    val = Validate("artem_podgorniy@yandex.ru")
    val.validate("artem_podgorniy@yandex.ru")
    dany = Boss(5782,"Dany","Soft Serve")
    maxim = Boss(6666,"Maxim","Beetroot")
    artem = Worker(7878,"Artem","Beetroot",maxim)
    vasyl = Worker(9999,"Vasyl","Soft Serve",dany)
    kolya = Worker(7777,"Kolya","Beetroot",maxim)
    print(maxim.workers_)
    @TypeDecorators.to_int
    def do_nothing(strr:str):
        return strr
    @TypeDecorators.to_bool
    def do_something(strr:str):
        return strr
    print(do_nothing("25"))
    print(do_nothing.__name__)
    print(do_something("true"))
