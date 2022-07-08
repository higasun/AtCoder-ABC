N = int(input())
ST = {}
for _ in range(N):
    s,t = input().split()
    ST[s] = int(t)

ST = sorted(ST.items(), key = lambda x: x[1])
print(ST[-2][0])