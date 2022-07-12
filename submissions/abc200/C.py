n = int(input())
a = [int(x) for x in input().split()]

def c(x):
    return x * (x - 1) // 2

cnt = [0]*200
for i in range(n):
    cnt[a[i]%200] += 1

ans = 0
for i in range(200):
    ans += c(cnt[i])

print(ans)