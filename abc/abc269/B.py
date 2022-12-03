s = [list(input()) for _ in range(10)]

a = None
b = None
c = None
d = None
for i in range(10):
    for j in range(10):
        if not a and s[i][j] == '#':
            a = i + 1
            c = j + 1
        elif not d and a and i == a-1:
            if s[i][j] == '.':
                d = j
            elif s[i][j] == '#' and j == 9:
                d = 10
        elif not b and a and j == c-1:
            if s[i][j] == '.':
                b = i
            elif s[i][j] == '#' and i == 9:
                b = 10

if a == 10 and not b:
    b = 10
if c == 10 and not d:
    d = 10
print(a, b)
print(c, d)