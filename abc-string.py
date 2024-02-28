# https://open.kattis.com/problems/abcstring
sentence = input()
map = {'A':0, 'B':0, 'C':0}
number = 0

for char in sentence:
    map[char] += 1
    number = max(number, map[char])
    if map['A'] >= 1 and map['B'] >= 1 and map['C'] >= 1:
        map['A'] -= 1
        map['B'] -= 1
        map['C'] -= 1
        
print(number)
    