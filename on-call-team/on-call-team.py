import math
import itertools

def solution(arr, n, m):
    for i in range(1, m+1):
        for subset in itertools.combinations(range(m), i):
            size = len(subset)
            # Check neighbors of subset corresponding to bit_string. 
            # Use Hall's theorem to check for perfect matching
            if not valid_neighbors(arr, subset, n, size):
                return print(size-1)
    print(m)
def valid_neighbors(arr, checked_elements, n, size):
    # Check if the checked elements have at least size neighbors
    workers = [False]*n
    for e in checked_elements:
        for i in range(n):
            if arr[e][i] == "1":
                workers[i] = True
    return sum(workers) >= size

n, m = map(int, input().split())
arr= []
for i in range(n):
    arr.append(list(input()))
# Transpose the array for easier access to columns
arr = list(map(list, zip(*arr)))

solution(arr, n, m)
    