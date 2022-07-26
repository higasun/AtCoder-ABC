n = int(input())
a = [input() for _ in range(n)]

ans = 'correct'
for i in range(n-1):
    for j in range(i+1, n):
        if a[i][j] == 'W' and a[j][i] != 'L':
            ans = 'incorrect'
            break
        elif a[i][j] == 'L' and a[j][i] != 'W':
            ans = 'incorrect'
            break
        elif a[i][j] == 'D' and a[j][i] != 'D':
            ans = 'incorrect'
            break
print(ans)