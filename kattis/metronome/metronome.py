a = int(input())
def solution(a):
    if a%1 != 0:
        return(f'{a/4:.2f}')
    else:
        return(a/4)
print(solution(a))