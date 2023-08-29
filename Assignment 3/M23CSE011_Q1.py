class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * self.size

    def hash1(self, key):
        return key % self.size

    def hash2(self, key):
        return 7 - (key % 7)

    def insert(self, key):
        index = self.hash1(key)
        if self.hash_table[index] is None:
            self.hash_table[index] = key
        else:
            offset = self.hash2(key)
            while self.hash_table[(index + offset) % self.size] is not None:
                offset += self.hash2(key)
            self.hash_table[(index + offset) % self.size] = key

    def lookup(self, key):
        index = self.hash1(key)
        offset = self.hash2(key)
        while self.hash_table[(index + offset) % self.size] is not None:
            if self.hash_table[(index + offset) % self.size] == key:
                return True
            offset += self.hash2(key)
        return False

    def delete(self, key):
        index = self.hash1(key)
        offset = self.hash2(key)
        while self.hash_table[(index + offset) % self.size] is not None:
            if self.hash_table[(index + offset) % self.size] == key:
                self.hash_table[(index + offset) % self.size] = None
                return


hash_table = DoubleHashingHashTable(10)

hash_table.insert(5)
hash_table.insert(15)
hash_table.insert(25)
hash_table.insert(8)

print(hash_table.lookup(15))
print(hash_table.lookup(10))

hash_table.delete(15)
print(hash_table.lookup(15))
