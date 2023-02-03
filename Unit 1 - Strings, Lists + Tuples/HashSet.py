class HashSet:

    def __init__(self):
        self.capacity = 3
        self.size = 0
        self.hashset = [None for _ in range(self.capacity)]

    def add(self, key: int) -> None:
        if self.size == self.capacity:
            self.rehash()

        index = key % self.capacity

        if self.hashset[index] == None:
            self.hashset[index] = key
            self.size += 1
        elif self.hashset[index] == key:
            return None
        else:
            newIndex = index
            while True:
                if self.hashset[newIndex] == None:
                    self.hashset[newIndex] = key
                    self.size += 1
                    return None
                else:
                    newIndex = (newIndex + 1) % self.capacity

                    if newIndex == index:
                        return None

        return None

    def rehash(self):
        self.capacity = 2 * self.capacity
        oldHashSet = self.hashset
        self.hashset = [None for _ in range(self.capacity)]

        for key in oldHashSet:
            if key:
                index = key % self.capacity
                self.hashset[index] = key

    def remove(self, key: int) -> None:
        index = key % self.capacity

        if self.hashset[index] == None:
            return None
        elif self.hashset[index] == key:
            self.hashset[index] = None
            self.size -= 1
            return None

    def contains(self, key: int) -> bool:
        index = key % self.capacity

        newIndex = index
        while True:
            if self.hashset[newIndex] == key:
                return True
            else:
                newIndex = (newIndex + 1) % self.capacity
                if newIndex == index:
                    return False

        return False

    def __str__(self):
        output = '{'
        for key in self.hashset:
            output += str(key) + ', '
        print('size', self.size)
        print('capacity', self.capacity)
        return output + '}'


        # Your MyHashSet object will be instantiated and called as such:
hashset = HashSet()
hashset.add(1)
hashset.add(11)
hashset.remove(11)
hashset.add(111)
print(hashset.contains(111))
print(hashset.contains(11111))
# hashset.add(111)
# hashset.add(1111)
# hashset.add(11111)
# hashset.add(111111)
# hashset.add(1111111)
print(hashset)
