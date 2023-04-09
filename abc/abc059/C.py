from collections import defaultdict

n = int(input())
cnt = defaultdict(int)
for i in range(n):
    if i == 0:
        for char in input():
            cnt[char] += 1
        continue

    crr_cnt = defaultdict(int)
    for char in input():
        crr_cnt[char] += 1
    for char, num in cnt.items():
        if i == 0:
            cnt[char] = crr_cnt[char]
        else:
            cnt[char] = min(cnt[char], crr_cnt[char])
cnt = sorted(cnt.items(), key=lambda x: x[0])
ans = ""
for char, num in cnt:
    ans += char*num
print(ans)
