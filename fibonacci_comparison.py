import time
import matplotlib.pyplot as plt
from functools import lru_cache

# -----------------------------
# 1. Fibonacci with LRU Cache
# -----------------------------

@lru_cache(maxsize=None)
def fibonacci_lru(n):
    if n < 2:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)

# -----------------------------
# 2. Splay Tree Implementation
# -----------------------------

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def _splay(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            if root.left is None:
                return root
            if key < root.left.key:
                root.left.left = self._splay(root.left.left, key)
                root = self._right_rotate(root)
            elif key > root.left.key:
                root.left.right = self._splay(root.left.right, key)
                if root.left.right:
                    root.left = self._left_rotate(root.left)
            return self._right_rotate(root) if root.left else root
        else:
            if root.right is None:
                return root
            if key > root.right.key:
                root.right.right = self._splay(root.right.right, key)
                root = self._left_rotate(root)
            elif key < root.right.key:
                root.right.left = self._splay(root.right.left, key)
                if root.right.left:
                    root.right = self._right_rotate(root.right)
            return self._left_rotate(root) if root.right else root

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
            return
        self.root = self._splay(self.root, key)
        if self.root.key == key:
            return
        new_node = Node(key, value)
        if key < self.root.key:
            new_node.right = self.root
            new_node.left = self.root.left
            self.root.left = None
        else:
            new_node.left = self.root
            new_node.right = self.root.right
            self.root.right = None
        self.root = new_node

    def search(self, key):
        self.root = self._splay(self.root, key)
        if self.root and self.root.key == key:
            return self.root.value
        return None

# -----------------------------
# 3. Fibonacci with Splay Tree
# -----------------------------

def fibonacci_splay(n, tree):
    result = tree.search(n)
    if result is not None:
        return result
    if n < 2:
        tree.insert(n, n)
        return n
    value = fibonacci_splay(n - 1, tree) + fibonacci_splay(n - 2, tree)
    tree.insert(n, value)
    return value

# -----------------------------
# 4. Performance Measurement
# -----------------------------

import timeit

n_values = list(range(0, 1000, 50))
lru_times = []
splay_times = []

for n in n_values:
    # Measure LRU Cache time
    start_time = time.time()
    fibonacci_lru(n)
    lru_times.append(time.time() - start_time)

    # Measure Splay Tree time
    tree = SplayTree()
    start_time = time.time()
    fibonacci_splay(n, tree)
    splay_times.append(time.time() - start_time)

# -----------------------------
# 5. Display Results
# -----------------------------

# a. Tabular Format
print(f"{'n':<10}{'LRU Cache Time (s)':<20}{'Splay Tree Time (s)':<20}")
print("-" * 50)
for n, lru, splay in zip(n_values, lru_times, splay_times):
    print(f"{n:<10}{lru:<20.10f}{splay:<20.10f}")

# b. Graphical Format
plt.plot(n_values, lru_times, label='LRU Cache')
plt.plot(n_values, splay_times, label='Splay Tree')
plt.xlabel('n')
plt.ylabel('Execution Time (s)')
plt.title('Fibonacci Computation Time Comparison')
plt.legend()
plt.grid(True)
plt.show()
