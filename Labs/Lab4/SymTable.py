from HashTable import HashTable

class SymbolTable:
    def __init__(self, size):
        self.__ht = HashTable(size)

    def __str__(self):
        return f"Symbol Table :\n{str(self.__ht)}"
    
    def put(self, key):
        pos = self.__ht.get(key)
        return pos if pos else self.__ht.put(key)