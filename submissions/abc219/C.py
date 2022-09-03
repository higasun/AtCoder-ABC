x = input()
n = int(input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'

c2i = {s: alphabet[i] for i, s in enumerate(x)}

def get_index(name):
    res = ''
    for c in name:
        res += c2i[c]
    return res

names = [input() for _ in range(n)]
names_index = [(name, get_index(name)) for name in names]
names_index.sort(key=lambda x: x[1])

for name, _ in names_index:
    print(name)