n = int(input())
s = [int(x) for x in input().split()]
t = [int(x) for x in input().split()]

for i in range(2*n):
    t[(i+1)%n] = min(t[(i+1)%n], t[i%n]+s[i%n])

for x in t: 
    print(x)