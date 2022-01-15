# task1
def with_index(iterable, start=0):
    for i in range(len(iterable)):
        yield start, iterable[i]
        start += 1


# task 2
def in_range(start, end, step):
    if step > 0:
        while start < end:
            yield start
            start += step
    elif step < 0:
        while start > end:
            yield start
            start += step
    else:
        raise ValueError("Canot be step 0")


# task3
class MyIterator:
    def __init__(self, iter_list, index=0):
        self.iter_list = iter_list
        self.index = index

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iter_list):
            rez = self.iter_list[self.index]
            self.index += 1
            return rez
        else:
            print("Stop Iteration")
            raise StopIteration

    def __getitem__(self, item):
        return self.iter_list[item]


if __name__ == '__main__':

    spisok = [3, 6, 8, 11, 52, 73,
              9, 77]
    # print(type(with_index))
    for i in with_index(spisok, 5):
        print(i)

    run = in_range(-2, -13, -2)
    for i in run:
        print(i)

    spisok1 = ["Kiev", "London", "Milan"]
    myiterator = MyIterator(spisok1)
    print(next(myiterator))
    print(next(myiterator))
    print(next(myiterator))
    print(myiterator[0:])