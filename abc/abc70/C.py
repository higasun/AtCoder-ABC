def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    return a // gcd(a, b) * b 

n = int(input())
t = []
for _ in range(n):
    t.append(int(input()))

ans = t[0]
for i in range(n-1):
    ans = lcm(ans, t[i+1])
print(ans)