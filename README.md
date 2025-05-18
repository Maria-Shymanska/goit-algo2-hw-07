task 1

# 📊 Optimizing Data Access Using LRU Cache

This project demonstrates how leveraging an LRU (Least Recently Used) cache can significantly enhance the efficiency of processing queries on a large array of data. We implement functions to compute the sum over a range and update array elements, both with and without caching, and compare their performance.

🚀 Usage

Generate an array of 100,000 random integers.

Create 50,000 random queries of types Range(L, R) and Update(index, value).

Process the queries without caching and then with LRU caching.

Measure and display the execution time for both approaches.

🧪 Functionality
The following functions are implemented:

range_sum_no_cache(array, L, R) – Computes the sum of elements in the range without caching.

update_no_cache(array, index, value) – Updates an element in the array without caching.

range_sum_with_cache(array, L, R) – Computes the sum of elements in the range using LRU cache.

update_with_cache(array, index, value) – Updates an element in the array and invalidates relevant cache entries.

📈 Results
After running the program, you will see output similar to:

Execution time without caching: 13.51 seconds
Execution time with LRU cache: 13.93 seconds
This demonstrates a significant performance improvement when using LRU caching for repeated queries.

task 2

## Fibonacci Performance Comparison: LRU Cache vs. Splay Tree

This task analyzes and compares the performance of computing Fibonacci numbers using two distinct methods:

LRU Cache: Utilizes Python's built-in functools.lru_cache decorator for memoization.

Splay Tree: Implements a self-adjusting binary search tree to store and retrieve previously computed Fibonacci numbers.

The goal is to measure and visualize the efficiency of both approaches across a range of input values.
