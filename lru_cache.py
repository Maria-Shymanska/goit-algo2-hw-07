import random
import time
from collections import OrderedDict

# Constants
N = 100_000
Q = 50_000
CACHE_SIZE = 1000

# Custom LRU Cache class
class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return None

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def invalidate(self, index):
        keys_to_delete = [k for k in self.cache if k[0] <= index <= k[1]]
        for k in keys_to_delete:
            del self.cache[k]

# Functions without cache
def range_sum_no_cache(array, L, R):
    return sum(array[L:R+1])

def update_no_cache(array, index, value):
    array[index] = value

# Functions with LRU cache
lru_cache = LRUCache(CACHE_SIZE)

def range_sum_with_cache(array, L, R):
    key = (L, R)
    result = lru_cache.get(key)
    if result is not None:
        return result
    result = sum(array[L:R+1])
    lru_cache.put(key, result)
    return result

def update_with_cache(array, index, value):
    array[index] = value
    lru_cache.invalidate(index)

# Generate random array and queries
array = [random.randint(1, 1000) for _ in range(N)]
queries = []
for _ in range(Q):
    if random.random() < 0.7:  # 70% Range, 30% Update
        L = random.randint(0, N - 2)
        R = random.randint(L, N - 1)
        queries.append(('Range', L, R))
    else:
        index = random.randint(0, N - 1)
        value = random.randint(1, 1000)
        queries.append(('Update', index, value))

# Run and time queries without cache
array_copy = array[:]
start_no_cache = time.time()
for q in queries:
    if q[0] == 'Range':
        range_sum_no_cache(array_copy, q[1], q[2])
    else:
        update_no_cache(array_copy, q[1], q[2])
end_no_cache = time.time()

# Run and time queries with cache
array_copy = array[:]
lru_cache = LRUCache(CACHE_SIZE)  # reset cache
start_with_cache = time.time()
for q in queries:
    if q[0] == 'Range':
        range_sum_with_cache(array_copy, q[1], q[2])
    else:
        update_with_cache(array_copy, q[1], q[2])
end_with_cache = time.time()

# Results
print(f"\nExecution time without caching: {end_no_cache - start_no_cache:.2f} seconds")
print(f"Execution time with LRU cache: {end_with_cache - start_with_cache:.2f} seconds")

