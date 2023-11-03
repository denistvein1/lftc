class HashTable():
    def __init__(self, size=100):
        self.size = size
        self.hashmap = [[] for _ in range(size)]

    def __str__(self):
        result = ""
        for i, bucket in enumerate(self.hashmap):
            result += f"{i} -> {bucket}\n"
        return result

    def _hash(self, key):
        total = 0
        for c in str(key):
            total += ord(c)
        return total % self.size

    def _get_index_and_bucket(self, key):
        index = self._hash(key)
        bucket = self.hashmap[index]
        return index, bucket

    def put(self, key):
        index, bucket = self._get_index_and_bucket(key)
        if key not in bucket:
            bucket.append(key)
            return index, len(bucket) - 1
        return False

    def get(self, key):
        index, bucket = self._get_index_and_bucket(key)
        if bucket and key in bucket:
            return index, bucket.index(key)
        return None

    def contains(self, key):
        index, bucket = self._get_index_and_bucket(key)
        return key in bucket

    def remove(self, key):
        index, bucket = self._get_index_and_bucket(key)
        if bucket and key in bucket:
            bucket.remove(key)
        else:
            raise KeyError(f"Key not found: {key}")

    def pos(self, key):
        index, bucket = self._get_index_and_bucket(key)
        for i, curr_key in enumerate(bucket):
            if curr_key == key:
                return index, i
        raise KeyError(f"Key not found {key}")
    
    def getSize(self):
        return self.size
    