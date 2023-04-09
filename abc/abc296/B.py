col = 'abcdefgh'
row = '87654321'
for i in range(8):
    s = input()
    for j in range(8):
        if s[j] == '*':
            ans = col[j] + row[i]
print(ans)
