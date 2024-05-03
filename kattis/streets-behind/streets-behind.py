# https://open.kattis.com/problems/streetsbehind
import math

def runs(n, k, a, b):
    ni = n
    num_runs = 0
    while ni < n + k:
        ni = min(math.floor((b/a)*ni), ni + k)
        k_added = min(math.floor((1 - a/b)*ni), k)
        num_runs += 1
        
    print(num_runs)
    
t = int(input())

tests = []
for _ in range(t):
    n, k, a, b = map(int, input().split())
    tests.append((n, k, a, b))

for test in tests:
    runs(test[0], test[1], test[2], test[3])