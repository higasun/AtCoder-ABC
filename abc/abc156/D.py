# x^n(mod m)の計算はpow(x, n, m)を使うこと
# nCr(mod m)は割り算に注意，逆元を計算する必要がある
# ModIntクラスを使っても良い

def inv(x, m):
    # inversed x (1/x) :mod m
    # オイラーの小定理から導ける
    return pow(x, m-2, m)

def nCr(n,r,m):
    aa = 1
    bb = 1
    for i in range(r):
        aa = aa*(n-i)%m
        bb = bb*(i+1)%m
 
    return a * inv(b, m) % m


n, a, b = map(int, input().split())
mod = 10**9+7

ans = pow(2, n, mod) - 1
ans -= nCr(n, a, mod)
ans -= nCr(n, b, mod)
print(ans % mod)