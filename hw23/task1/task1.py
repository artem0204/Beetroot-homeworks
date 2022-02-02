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

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._stack), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()

def revers_order(seq):
    rev_seq = ""
    s = Stack()
    for i in seq:
        s.push(i)
    for n in seq:
        rev_seq += s.pop()
    return rev_seq


if __name__=="__main__":
    print(revers_order("Hello world"))

