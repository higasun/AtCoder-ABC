from bisect import bisect_left

n = int(input())
s = input()
w = list(map(int, input().split()))
ads = list()
chn = list()
for i, c in enumerate(s):
    if c == '0':
        chn.append(w[i])
    else:
        ads.append(w[i])
if len(chn) == 0 or len(ads) == 0:
    print(n)
    exit()

chn.sort()
ads.sort()
ans = 0
for x in w:
    crr = bisect_left(chn, x)
    crr += len(ads) - bisect_left(ads, x)
    ans = max(ans, crr)
print(ans)
