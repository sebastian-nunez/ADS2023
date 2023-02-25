class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashMap:

    def __init__(self):
        self.capacity = 10
        self.size = 0
        self.hashmap = [None for _ in range(self.capacity)]

    def put(self, key: int, value: int) -> None:
        if self.size == self.capacity:
            self.rehash()

        i = key % self.capacity

        if self.hashmap[i] == None:
            self.hashmap[i] = Pair(key, value)
            self.size += 1
            return None
        elif self.hashmap[i].key == key:
            self.hashmap[i].value = value
            return None
        else:
            i = (i + 1) % self.capacity
            start = i
            while True:
                if self.hashmap[i] == None:
                    self.hashmap[i] = Pair(key, value)
                    self.size += 1
                    return None
                elif self.hashmap[i].key == key:
                    self.hashmap[i].value = value
                    return None
                else:
                    i = (i + 1) % self.capacity
                    if i == start:
                        return None

    def rehash(self):
        self.capacity = 2 * self.capacity
        oldHashSet = self.hashmap
        self.hashset = [None for _ in range(self.capacity)]

        for pair in oldHashSet:
            if pair:
                i = pair.key % self.capacity
                self.hashset[i] = pair

    def get(self, key: int) -> int:
        i = key % self.capacity

        if self.hashmap[i] == None:
            return -1
        elif self.hashmap[i].key == key:
            return self.hashmap[i].value
        else:
            i = (i + 1) % self.capacity
            start = i
            while True:
                if self.hashmap[i].key == key:
                    return self.hashmap[i].value
                else:
                    i = (i + 1) % self.capacity
                    if i == start:
                        return -1

    def remove(self, key: int) -> None:
        i = key % self.capacity
        self.hashmap[i] = None
        self.size -= 1

        return None

    def __str__(self):
        output = '{'
        for pair in self.hashmap:
            if pair:
                output += f'{pair.key}: {pair.value}, '

        return output + '}'


# Your MyHashMap object will be instantiated and called as such:
hashmap = HashMap()
hashmap.put(1, 20)
hashmap.put(3, 24)
print(hashmap)
print(hashmap.get(3))
print(hashmap.get(0))
print(hashmap.remove(1))
print(hashmap)
print(hashmap.get(1))

#%%
