class Stack:
    def __init__(self):
        self._stack = []
        self._ind = -1

    def is_empty(self):
        return bool(self._stack)

    def __iter__(self):
        return self

    def __next__(self):
        self._ind += 1
        if self._ind == len(self._stack):
            raise StopIteration
        else:
            return self._stack[self._ind]

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        return self._stack.pop()

    def peek(self):
        return self._stack[len(self._stack) - 1]

    def size(self):
        return len(self._stack)

    def get_from_stack(self, el):
        try:
            return self._stack.index(el)
        except ValueError:
            raise Exception(f"Your {el} not found in stack")

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._stack), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()


class Queue:
    def __init__(self):
        self._items = []
        self.ind = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.ind += 1
        if self.ind == len(self._items):
            raise StopIteration
        return self._items[self.ind]

    def get_from_queue(self, el):
        try:
            return self._items.index(el)
        except ValueError:
            raise Exception(f"Your {el} not found in queue")

    def is_empty(self):
        return bool(self._items)

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Queue>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    s = Stack()
    s.push("a")
    s.push("t")
    s.push("7")
    s.push("h")
    print(s.get_from_stack("h"))

    q = Queue()
    q.enqueue("5")
    q.enqueue("4")
    q.enqueue("6")
    q.enqueue("9")
    print(q.get_from_queue("6"))