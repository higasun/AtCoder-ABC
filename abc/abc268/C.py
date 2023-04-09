n = int(input())
p = list(map(int, input().split()))
c = [0]*n
for i, x in enumerate(p):
    c[(x-1-i)%n] += 1
    c[(x-i)%n] += 1
    c[(x+1-i)%n] += 1
print(max(c))
