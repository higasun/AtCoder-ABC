n,k = map(int, input().split())
a = []
a.append([0]*(n+2))
for _ in range(n):
    tmp = list(map(int, input().split()))
    a.append([0]+tmp+[0])
a.append([0]*(n+2))

#答えで二分探索
l = 0
r = 10**9+1
while r - l > 1:
  
    m = (r+l)//2

    # aをmの大小でbit化
    b = [[0]*(n+2) for _ in range(n+2)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if a[i][j] >= m:
                b[i][j] = 1

    #二次元の累積和をとる
    #右方向
    for i in range(1,n+1):
        for j in range(1,n+1):
            b[i][j] += b[i][j-1]
    
    #下方向
    for j in range(1,n+1):
        for i in range(1,n+1):
            b[i][j] += b[i-1][j]
    
    check = 1
    for i in range(1, n-k+2):
        for j in range(1, n-k+2):
            tmp = b[i+k-1][j+k-1] - b[i+k-1][j-1] - b[i-1][j+k-1] + b[i-1][j-1]

            if tmp < k**2//2+1:
                check = 0

    if check == 1:
        l = m
    else:
        r = m

print(l)

