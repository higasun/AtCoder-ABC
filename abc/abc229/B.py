a, b = map(int, input().split())
ans = 'Easy'
while (a > 0 and b > 0):
    if a % 10 + b % 10 >= 10:
        ans = 'Hard'
        break
    a //= 10
    b //= 10
print(ans)
