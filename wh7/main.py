# task 1
def oops():
    try:
        [12, 73][3]
    except IndexError:
        print("elements of list is out of range")


def oops_second():
    try:
        oops()
    except KeyError:
        print("Happend Key eror")


# task2
def division(a, b):
    try:
        return a ** 2 / b
    except TypeError:
        return "find type error exception "
    except ZeroDivisionError:
        return "find Zero Division error "


# task additionally
def joinA(*args):
    rez = ""
    for i in args:
        rez +=i + "A"
    print(rez)

if __name__ == '__main__':
    oops()
    oops_second()
    num1 = input("enter firs number ")
    num2 = int(input("enter second number"))
    print(division(num1, num2))
    joinA("hello","Artem")
