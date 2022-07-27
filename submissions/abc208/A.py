a, b = map(int, input().split())
ans = 'No'
if a <= b <= 6*a:
    ans = 'Yes'
print(ans)