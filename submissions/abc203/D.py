n,k = map(int, input().split())
a = []
a.append([0]*(n+2))
for _ in range(n):
    tmp = list(map(int, input().split()))
    a.append([0]+tmp+[0])
a.append([0]*(n+2))

#最適な中央値を二分探索
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

    #二次元累積和
    #右方向
    for i in range(1,n+1):
        for j in range(1,n+1):
            b[i][j] += b[i][j-1]
    
    #下方向
    for j in range(1,n+1):
        for i in range(1,n+1):
            b[i][j] += b[i-1][j]
    
    #check: 中央値がm未満となるようなカーネルが存在するか
    check = False
    for i in range(1, n-k+2):
        for j in range(1, n-k+2):
            tmp = b[i+k-1][j+k-1] - b[i+k-1][j-1] - b[i-1][j+k-1] + b[i-1][j-1]

            if tmp < k**2//2+1: # <=> bのカーネル内の中央値が0 <=> aのカーネル内の中央値がm未満
                check = True

    if check: 
        r = m
    else: 
        l = m

print(l)

