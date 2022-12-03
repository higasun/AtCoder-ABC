from collections import defaultdict

n = int(input())
a = [int(x) % 200 for x in input().split()]

n = min(n, 8)
d = defaultdict(list)
for bit in range(1, 2**n):
    rem = 0
    for i in range(n):
        if (1 << i) & bit:
            rem += a[i]
            rem %= 200
    d[rem].append(bit)

exist = False
for v in d.values():
    if len(v) >= 2:
        print('Yes')

        bit1, bit2 = v[0], v[1]      
        ans1, ans2 = [], []
        for i in range(n):
            if (1 << i) & bit1:
                ans1.append(str(i+1))
            if (1 << i) & bit2:
                ans2.append(str(i+1))
        print(len(ans1), ' '.join(ans1))
        print(len(ans2), ' '.join(ans2))

        exist = True
        break

if not exist:
    print('No')