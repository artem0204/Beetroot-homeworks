from functools import wraps

if __name__ == '__main__':
    def logger(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            rez = func(*args, **kwargs)
            print(f"{func.__name__},called with {args}")

        return wrapper


    @logger
    def add(x, y):
        return x + y


    @logger
    def square_all(*args):
        return [arg ** 2 for arg in args]


    add(4, 5)
    print(add.__name__)
    square_all(4, 5, 6, 7)


# task2
def stop_words(list_param=["pepsi", "BMW"]):
    def inner_function(func):
        def wrap(*args, **kwargs):
            decorated_str = func(*args, **kwargs)
            for word in list_param:
                decorated_str = decorated_str.replace(word, "*")
            print(decorated_str)
            return decorated_str

        return wrap

    return inner_function


@stop_words()
def create_slogan(name):
    return f"{name},drinks pepsi in his brand BMW !"


create_slogan("Mike")


@stop_words(list_param=["drinks", "brand"])
def another_slogan(name):
    return f"{name},drinks pepsi in his brand BMW !"


another_slogan("Karl")

# task3

def arg_rules(type_ , max_length, contains):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            for arg in args:
                if type(arg) is not type_:
                    print("Wrong type ")
                    return False
                if len(arg) > max_length:
                    print("very long")
                    return False
                for item in contains:
                    if item not in arg:
                        print("dosent containe some of required symbols ")
                        return False
            print(func(*args, **kwargs))
            return func(*args, **kwargs)
        return wrapper
    return decorator

@arg_rules(type_=str,max_length= 15 , contains= ["05","@"])
def create_slogan(name):
    """this is function prints some text with name"""
    return f"{name}, drinks pepsi in his brand new BMW !"

create_slogan("nv4njvnjn")
create_slogan("j3rnjnwv")
create_slogan(1)
create_slogan("artem05@")
print(create_slogan.__name__)
print(create_slogan.__doc__)
