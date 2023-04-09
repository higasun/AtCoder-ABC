def next_permutation(a: list):
    """
    Returns next permutation
    Time complexity: O(n)
    """
    n = len(a)
    for i in range(n-1, 0, -1):
        if a[i-1] < a[i]:
            x = i-1
            break
    for i in range(n-1, 0, -1):
        if a[x] < a[i]:
            a[i], a[x] = a[x], a[i]
            break
    return a[:x+1] + a[n-1:x:-1]

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
a = -1
b = -1
v = list(range(1, n+1))
idx = 1
while (a < 0 or b < 0):
    ok = True
    for i in range(n):
        if v[i] != p[i]:
            ok = False
            break
    if ok:
        a = idx

    ok = True
    for i in range(n):
        if v[i] != q[i]:
            ok = False
            break
    if ok:
        b = idx

    v = next_permutation(v)
    idx += 1

print(abs(a-b))
