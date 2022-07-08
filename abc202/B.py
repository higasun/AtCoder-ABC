s = list(input())

s = s[::-1]
for i, c in enumerate(s):
    if c == '6':
        s[i] = '9'
    elif c == '9':
        s[i] = '6'

print(''.join(s))