import math

def solution(arr, n, m):
    bit_strings = []
    broken = float("inf")
    for i in range(int(math.pow(2, m))):
        # Get the bit string of i
        bit_string = ("0" * (m - len(bin(i)[2:])) + bin(i)[2:])
        size = sum([int(x) for x in bit_string])
        
        # Check neighbors of subset corresponding to bit_string. 
        # Use Hall's theorem to check for perfect matching
        checked_elements = [i for i, x in enumerate(bit_string) if x == "1"]
        if not valid_neighbors(arr, checked_elements, n, size):
            broken = min(broken, size)
    if broken == float("inf"):
        print(m)
    else:
        print(broken-1)
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
    