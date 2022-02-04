


class Stack:
    class Node:
        def __init__(self, data, nextNode):
            self.data = data
            self.nextNode = nextNode

    def __init__(self):
        self._head = None

    def isEmpty(self):
        return self._head is None

    def push(self, value):
        self._head = Stack.Node(value, self._head)

    def pop(self):
        if self.isEmpty():
            raise IndexError("Index is our of range")
        val = self._head.data
        self._head = self._head.nextNode
        return val



if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.pop()



    while not s.isEmpty():
        print(s.pop())
