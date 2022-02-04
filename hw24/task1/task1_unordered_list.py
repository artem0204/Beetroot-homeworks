from task1.task1_node import Node


class UnorderedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def append(self, item):
        temp = Node(item)
        current = self._head
        if current == None:
            self._head = temp
            return self._head

        while current.get_next() != None:
            current = current.get_next()
        current.set_next(temp)

    def pop(self):
        current = self._head
        while current.get_next().get_next() != None:
            current = current.get_next()
        current.set_next(None)

    def index(self,index):
        current = self._head
        count = 0
        while current != None:
            if count == index:
                return current.get_data()
            count += 1
            current = current.get_next()
        print("index is out of range ")

    def insert(self,index,data):
        temp = Node(data)
        current = self._head
        count = 0
        while current.get_next() != None:
            if index == 0:
                self.add(data)
            elif count + 1 == index:
                after_current = current.get_next()
                current.set_next(temp)
                temp.set_next(after_current)
                return temp.get_data()
            count += 1
            current = current.get_next()
        print("Index is out of range")

    def slice(self,start = 0 , stop = 0 ):
        if  start > self.size() or stop > self.size():
            raise IndexError("Index is out of range ")
        current = self._head
        counter = 0
        res = ""
        if start == 0 and stop == 0 :
            self.__repr__()
        elif start != 0 :
            while counter < start:
                current = current.get_next()
                counter += 1
        while counter < stop:
            res += str(current.get_data())+"->"
            current = current.get_next()
            counter += 1
        return res




    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    my_list = UnorderedList()
    my_list.append(5)
    my_list.append(3)
    my_list.append(1)
    my_list.pop()
    print(my_list.insert(1,7))
    print(my_list.slice(1,3))

    print(my_list)

    # my_list.add(31)
    # my_list.add(77)
    # my_list.add(17)
    # my_list.add(93)
    # my_list.add(26)
    # my_list.add(54)
    # print(my_list.get_node_by_index(77))
    #
    # print(my_list.size())
    # print(my_list)
    # print(my_list.search(93))
    # print(my_list.search(100))
    #
    # my_list.add(100)
    # print(my_list)
    # print(my_list.search(100))
    # print(my_list.size())
    #
    # my_list.remove(54)
    # print(my_list.size())
    # my_list.remove(93)
    # print(my_list.size())
    # my_list.remove(31)
    # print(my_list.size())
    # print(my_list.search(93))
