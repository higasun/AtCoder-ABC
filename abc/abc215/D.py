import math

n, m = map(int, input().split())
a = [int(x) for x in input().split()]

def get_prime(x):
    res = []
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            while x % i == 0:
                x //= i
            res.append(i)
    if x > 1:
        res.append(x)
    return res

prime = [True]*(100005)
for i in range(n):
    l = get_prime(a[i])
    for x in l:
        if not prime[x]: continue
        y = x
        while y <= m:
            prime[y] = False
            y += x

print(sum(prime[1:m+1]))
for i in range(1, m+1):
    if prime[i]:
        print(i)