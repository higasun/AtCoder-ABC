n, k = map(int, input().split())

ans = 0
for i in range(1, n+1): 
    ans += 100 * i * k

for i in range(1, k+1):
    ans += i * n

print(ans)