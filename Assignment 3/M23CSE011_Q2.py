class ChainingHashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        self.hash_table[index].append(key)

    def lookup(self, key):
        index = self.hash_function(key)
        return key in self.hash_table[index]

    def delete(self, key):
        index = self.hash_function(key)
        if key in self.hash_table[index]:
            self.hash_table[index].remove(key)

hash_table = ChainingHashTable(10)

hash_table.insert(5)
hash_table.insert(15)
hash_table.insert(25)
hash_table.insert(8)

print(hash_table.lookup(15))
print(hash_table.lookup(10))

hash_table.delete(15)
print(hash_table.lookup(15))

