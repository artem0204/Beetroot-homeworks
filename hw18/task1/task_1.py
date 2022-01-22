import datetime as dt


class Open:
    counter = 0

    def __init__(self, file_name, mode="r"):
        self.file_name = file_name
        self.mode = mode
        self.file = open(file_name, mode)
        self.logger = open("logger.txt", "a")

    def __enter__(self):
        self.logger.writelines(f"opened. file name:{self.file_name}, mode:{self.mode}, time:{dt.datetime.now().time()}\n")
        self.__class__.counter += 1
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        self.logger.writelines(f"closed. file name:{self.file_name}, mode:{self.mode}, time:{dt.datetime.now().time()}\n")
        self.logger.close()
        return None

    @classmethod
    def get_counter(cls):
        return cls.counter


with Open("some_file.txt", "w") as file:
    file.write("some_txt")
    print("count:",Open.get_counter())
    file.close()
with Open("some_file.txt", "w") as file:
    file.write("some text")
    print("count:",Open.get_counter())
    file.close()
