class Map:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.bucket = [[] for _ in range(capacity)]
        self.size = 0
       
    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, val):
        index = self._hash(key)
        bucket = self.bucket[index]

        # verificăm dacă cheia deja există → update
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, val)
                return

        # altfel, dacă nu există → inserăm
        bucket.append((key, val))
        self.size += 1        

    def get(self, key):
        index = self._hash(key)
        bucket = self.bucket[index]

        for k, v in bucket:
            if k == key:
                return v
        return None      

    def remove(self, key):
        index = self._hash(key)
        bucket = self.bucket[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]   
                self.size -= 1
                return True
        return False           

    def containsKey(self, key):
        index = self._hash(key)
        bucket = self.bucket[index]

        for k, _ in bucket:
            if k == key:
                return True
        return False

m = Map()

m.put('name', 'Ana')
m.put('city', 'Cluj')
m.put('age', 35)
m.put('status', 'married')

print(m.get('name'))
print(m.get('city'))
print(m.get('age'))
print(m.get('status'))
print(m.containsKey('lastname'))
print(m.containsKey('name'))

print(m.remove('name'))
print(m.get('name'))

print(m.put('name','Maria'))
print(m.get('name'))