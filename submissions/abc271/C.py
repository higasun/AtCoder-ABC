from collections import defaultdict

n = int(input())
d = defaultdict(int)
a = [int(x)-1 for x in input().split()]
for i in range(n):
    d[a[i]] += 1

remain = n
ans = 0
while remain > 0:
    if d[ans] > 0:
        remain -= 1
        ans += 1
    elif remain >= 2:
        remain -= 2
        ans += 1
    else:
        break
    

    

print(ans)