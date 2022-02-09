class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __repr__(self):
        return f"{self.key}=>{self.val}"


class HashTable:
    def __init__(self, size):
        self.size = size
        self.items = [None] * self.size

    def hash_func(self, key):
        if isinstance(key, int):
            return key % self.size
        elif isinstance(key, str):
            return sum([ord(char) for char in key]) % self.size
        raise TypeError(f"Wrong {key} of type {type(key)}")

    def rehash(self, index):
        return (index + 1) % self.size

    def put(self, key, value):
        new_data = Node(key, value)
        index = self.hash_func(key)
        start = index
        while self.items[index]:
            index = self.rehash(index)
            if index == start:
                raise IndexError("Hash table is fully filled")
        self.items[index] = new_data

    def get(self, key):
        index = self.hash_func(key)
        start = index
        while self.items[index]:
            if self.items[index].key == key:
                return self.items[index].value
            else:
                index = self.rehash(index)
            if index == start:
                raise IndexError(f"No data with such key: {key}")

    def delete(self, key):
        index = self.hash_func(key)
        while self.items[index]:
            if self.items[index].key == key:
                self.items[index] = None
                return
            else:
                index = self.rehash(index)

    def __contains__(self, key):
        index = self.hash_func(key)
        start = index
        while True:
            if self.items[index] and self.items[index].key == key:
                return True
            else:
                index = self.rehash(index)
            if index == start:
                break
        for node in self.items:
            if node and node.value == key:
                return True
        return False

    def __len__(self):
        counter = 0
        temp = self.items.copy()
        while temp:
            counter += 1
            temp.pop()
        return counter



if __name__ == "__main__":
    h = HashTable(11)
    print(type(h.items))
    h.put(45,"abc")
    h.put(22,"cd")
    h.put(33,"bca")
    h.put(34,"bca")
    h.put(35, "bca")
    h.put(36, "bca")
    h.put(37, "bca")
    h.put(38, "bca")
    h.put(39, "bca")
    h.put(40, "bca")
    h.put(41, "bca")
    print(h.items)
    print(h.__contains__(35))
    print(h.__len__())
    h.delete(41)
    print(h.items)