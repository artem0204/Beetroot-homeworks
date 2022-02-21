from task1.task1 import BinaryHeapMax
class PriorityQueue(BinaryHeapMax):
    def __init__(self)-> None:
        super().__init__()
    def enqueue(self,value):
        self.insert(value)
    def dequeue(self):
        return self.pop_max()


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.enqueue(1)
    pq.enqueue(2)
    pq.enqueue(6)
    print(pq.heap_list)
    print(pq.dequeue())
