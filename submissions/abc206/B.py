n = int(input())

l = 0
r = 10 ** 9
while r - l > 1:
    m = (r+l)//2
    if m * (m+1) // 2 >= n: r = m
    else: l = m
print(r)
