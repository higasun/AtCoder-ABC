from math import factorial

def f(a, b):
    return factorial(a+b) // (factorial(a) * factorial(b))

a, b, k = map(int, input().split())

ans = ''
for i in range(a + b):
    if a == 0:
        ans += 'b'
        continue
    elif b == 0:
        ans += 'a'
        continue

    if f(a-1, b) >= k: # 'a~'の場合
        ans += 'a'
        a -= 1
    else:                    # 'b~'の場合
        ans += 'b'
        k -= f(a-1, b)
        b -= 1


print(ans)