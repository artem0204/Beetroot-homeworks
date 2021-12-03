# task1
movie = "forsage"


def favorite_movie(x):
    print("my favorite movie is", x)


favorite_movie(movie)


# task2

def make_country(country, capital):
    slovar = {country: capital}
    print(slovar)


make_country("ukraine", "kiev")

# task3

def make_operation(operator, *args):
    rez = 0
    rez1 = 1
    for i in args:
        if operator == "+":
            rez += i
        elif operator == "-":
            rez -= i
        elif operator == "*":
            rez1 *= i
    return rez,rez1

print(make_operation("+", 3, 4, 8, 33))
print(make_operation("-", 5, 5, -10, -20))
print(make_operation("*", 6, 7))
