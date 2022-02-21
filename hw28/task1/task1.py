class BinaryHeapMax:
    def __init__(self):
        self.heap_list = [0]
        self.heap_size = 0

    def _move_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] > self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i //= 2

    def insert(self, key):
        self.heap_list.append(key)
        self.heap_size += 1
        self._move_up(self.heap_size)

    def _move_down(self, i):
        while i * 2 < self.heap_size:
            max_child_index = self._search_max_child(i)
            if self.heap_list[i] < self.heap_list[max_child_index]:
                self.heap_list[i], self.heap_list[max_child_index] = self.heap_list[max_child_index], self.heap_list[i]
            else:
                break
            i = max_child_index

    def _search_max_child(self, i):
        if i * 2 + 1 > self.heap_size:
            return i * 2
        else:
            if self.heap_list[i*2]>self.heap_list[i*2+1]:
                return i*2
            else:
                return i*2+1
    def pop_max(self):
        max_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.heap_size]
        self.heap_list.pop()
        self.heap_size-=1
        self._move_down(1)
        return max_value
    def build_heap(self,li):
        self.heap_list = [0]+li[:]
        self.heap_size = len(li)
        i = self.heap_size//2
        while i > 0 :
            self._move_down(i)
            i -= 1


if __name__ == "__main__":
    bh = BinaryHeapMax()
    bh.insert(10)
    bh.insert(15)
    bh.insert(12)
    bh.insert(5)
    bh.insert(1)
    bh.insert(6)
    bh.insert(2)
    print(bh.heap_list)
    print(bh.pop_max())
    bh.build_heap([23,41,117,5,1,6,2])
    print(bh.heap_list)
