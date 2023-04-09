from math import gcd

n = int(input())
towns = [tuple(map(int, input().split())) for _ in range(n)]

magic = set()

for i in range(n-1):
    for j in range(i+1, n):
        xi, yi = towns[i]
        xj, yj = towns[j]
        
        g = gcd((xj-xi), (yj-yi))
        i2j = ((xj-xi) / g, (yj-yi) / g)

        g = gcd((xi-xj), (yi-yj))
        j2i = ((xi-xj) / g, (yi-yj) / g)

        magic.update({i2j, j2i})

print(len(magic))