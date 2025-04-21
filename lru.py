"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, 
add the key-value pair to the cache. 
If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Analysis:
1. Initialization: create a dictionary with keys in range capacity and value as none
2. put: insert the value for the given key in the dictionary. Time complexity will be O(1) execpt for the remove function
    as it has to find the key in the list to remove it. # TODO: O(1) can be acheived with a doubly linked list.
3. get: return the value for a given key, otherwise return -1 if it does not exist. Same time complexity
4. Space complexity will be O(capacity) since it depends on what capacity is a passed.
"""

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru = []
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.lru.remove(key)
            self.lru.append(key)
            return self.cache[key]
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.lru.remove(key)
        elif len(self.cache) == self.capacity:
            lru_key = self.lru.pop(0)
            del self.cache[lru_key]
        self.cache[key] = value
        self.lru.append(key)





# Test case
obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
obj.get(1)
obj.put(3, 3)
print(obj.get(2))

