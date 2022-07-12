n = int(input())
a = [int(x) for x in input().split()]

check = [False]*(n+1)
for i in range(n):
    check[a[i]] = True

flg = True
for i in range(1, n+1):
    if not check[i]:
        flg = False

print('Yes' if flg else 'No')