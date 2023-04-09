n, m = map(int, input().split())
a = []
for i in range(m):
    c = int(input())
    a.append(set(map(int, input().split())))

ans = 0
for i in range(1, 2**m):
    nums = set()
    for j in range(m):
        if (i >> j) & 1:
            nums = nums.union(a[j])
    ans += int(len(nums) == n)
print(ans)