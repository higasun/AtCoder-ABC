n, q = map(int, input().split())
s = input()
cusum = [0]*n
for i in range(1, n):
    if s[i-1:i+1] == "AC":
        cusum[i] += cusum[i-1]+1
    else:
        cusum[i] = cusum[i-1]

for _ in range(q):
    l, r = map(int, input().split())
    print(cusum[r-1] - cusum[l-1])