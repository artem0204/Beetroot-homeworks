class Node:
    def __init__(self, data, ):
        self.data = data
        self.nextNode = None
class Queue:


    def __init__(self):
        self._head = None
        self.last = None

    def isEmpty(self):
        return self._head is None

    def enqueue(self, value):
        if self.last is None:
            self._head = Node(value)
            self.last = self._head
        else:
            self.last.nextNode = Node(value)
            self.last = self.last.nextNode



    def dequeue(self):
        if self._head is None:
            return None
        else:
            rez = self._head.data
            self._head = self._head.nextNode
            return rez



if __name__ == "__main__":
    q =Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.dequeue()




    while  not q.isEmpty():
        print(q.dequeue())