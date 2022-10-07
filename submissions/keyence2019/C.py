n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

d = []
total = 0
for i in range(n):
    diff = a[i] - b[i]
    total += diff
    d.append(diff)

if total < 0:
    print(-1)
else:
    ans = [False]*n
    cur = n-1
    d.sort()
    for i in range(n):
        if d[i] >= 0:
            break
        ans[i] = True
        while d[i] < 0:
            ans[cur] = True
            if d[cur] > abs(d[i]):
                d[cur] -= abs(d[i])
                d[i] = 0
            else:
                d[i] += d[cur]
                d[cur] = 0
                cur -= 1


    print(sum(ans))