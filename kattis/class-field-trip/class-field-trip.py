a = input()
b = input()
def solution(a, b):
    x = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            x.append(a[i])
            i+=1
        else:
            x.append(b[j])
            j+=1
    x.extend(a[i:])
    x.extend(b[j:])
    return "".join(x)
solution(a, b)