import math

def runs(n, k, a, b):
    ni = n
    num_runs = 0
    while ni < n + k:
        ni = math.floor((b/a)*ni)
        num_runs += 1
    print(num_runs)
    
t = int(input())

for _ in range(t):
    n, k, a, b = map(int, input().split())
    runs(n, k, a, b)   