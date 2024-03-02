import math
import itertools

def solution(arr, n, m):
    memo = memoize(arr, n, m)
    # Try all possible subsets of tasks
    for i in range(1, m+1):
        for subset in itertools.combinations(range(m), i):
            size = len(subset)
            # Use Hall's Marriage theorem to check for perfect matching
            if not valid_neighbors(memo, subset, size):
                return print(size-1)
    return print(m)
    
def memoize(arr, n, m):
    # Create a memoization table to store the number of neighbors for each element
    memo = [set() for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if arr[i][j] == "1":
                memo[i].add(j)
    return memo

def valid_neighbors(memo, checked_elements, size):
    # Check if the checked elements have at least size neighbors
    neighbors = set()
    for i in checked_elements:
        neighbors = neighbors.union(memo[i])
        if len(neighbors) >= size:
            return True
    return len(neighbors) >= size

n, m = map(int, input().split())
arr= []
for i in range(n):
    arr.append(list(input()))
# Transpose the array for easier access to columns
arr = list(map(list, zip(*arr)))

solution(arr, n, m)
    