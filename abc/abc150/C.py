from math import factorial

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

def f(a: list):
    if len(a) == 1:
        return 1
    else:
        x = a[0]
        y = sorted(a).index(x)
        cnt = y * factorial(len(a)-1) + f(a[1:])
        return cnt

a = f(p)
b = f(q)
print(abs(a-b))
