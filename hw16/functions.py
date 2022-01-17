# task1
movie = "forsage"
def favorite_movie(x):
    return f"my favorite movie is {x}"

# task2

def make_country(country, capital):
    slovar = {country: capital}
    return slovar

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
    return rez, rez1
