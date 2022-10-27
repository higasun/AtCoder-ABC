# 最大公約数(ユークリッドの互助法): O(log(max(a, b)))
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

# 最小公倍数(LG = ab を利用)
def lcm(a, b):
    return a // gcd(a, b) * b