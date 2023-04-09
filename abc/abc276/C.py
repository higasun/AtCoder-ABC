n = int(input())
p = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    if p[i-1] > p[i]:
        q = p[i-1:]
        p = p[:i-1]
        break

x = q[0]
q.sort(reverse=True)
y = q.index(x) + 1
r = [q[y]] + q[:y] + q[y+1:]

ans = p + r
print(" ".join(map(str, ans)))
