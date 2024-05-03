import numpy as np

count = input()
a, b = count.split()
a = int(a)
b = int(b)
x = []
rung = input()
while rung:
    x.append(int(rung))
    rung = input()
table = np.zeros((b, a))
for i in range(b):
    table[i, x[i] - 1] = 1


def solution():
    answers = [None] * a
    for i in range(a):
        x_pos = i
        y_pos = 0
        while y_pos < b:
            if table[y_pos][x_pos] == 1:
                x_pos += 1
            elif table[y_pos][x_pos - 1] == 1:
                x_pos -= 1
            y_pos += 1
        answers[x_pos] = i + 1
    for answer in answers:
        print(answer)

solution()
