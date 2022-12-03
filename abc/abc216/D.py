from collections import deque

n, m = map(int, input().split())
a = []
for i in range(m):
    k = int(input())
    l = deque(int(x)-1 for x in input().split())
    a.append(l)

pos = [[] for _ in range(n)]
cnt = [0]*n
que = deque()

for i in range(m):
    cnt[a[i][0]] += 1
    pos[a[i][0]].append(i)
    if cnt[a[i][0]] >= 2:
        que.append(a[i][0])

flg = [False]*n

while que:
    x = que.popleft()
    flg[x] = True

    cnt[x] -= 2
    i1, i2 = pos[x]
    a[i1].popleft()
    a[i2].popleft()
    if a[i1]:
        cnt[a[i1][0]] += 1
        pos[a[i1][0]].append(i1)
        
        if cnt[a[i1][0]] >= 2:
            que.append(a[i1][0])
            
    if a[i2]:
        cnt[a[i2][0]] += 1
        pos[a[i2][0]].append(i2)

        if cnt[a[i2][0]] >= 2:
            que.append(a[i2][0])

if sum(flg) >= n:
    print("Yes")
else:
    print("No")