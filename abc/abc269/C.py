n = int(input())
d = []
n_ = n
for i in range(60):
    if n_ == 1:
        d.append(i)
        break
    if n_ % 2 == 1:
        d.append(i)
    n_ //= 2

ans = []
len_d = len(d)
for i in range(2**len_d):
    entry = ['0' for _ in range(61)]
    for j in range(len_d):
        if (i >> j) & 1:
            entry[-(d[j]+1)] = '1'
    
    entry = '0b' + ''.join(entry)
    ans.append(int(entry, 0))

for a in ans:
    print(a)