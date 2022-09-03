n = int(input())
v = [tuple(map(int, input().split())) for _ in range(n)]
v.sort()

def check(target: tuple):
    l, r = 0, n-1
    while r - l > 1:
        mid = (r + l) // 2
        if v[mid] <= target:
            l = mid
        else:
            r = mid
    return target == v[l]
    
ans = 0
for i in range(n):
    for j in range(n):
        if v[i][0] < v[j][0] and v[i][1] < v[j][1]:
            if check((v[i][0], v[j][1])) and check((v[j][0], v[i][1])):
                ans += 1
print(ans)