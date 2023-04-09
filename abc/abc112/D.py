def enum_divisors(n):
    """
    Enumerate divisors of n
    Time complexity: O(√n)
    """
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


n, m = map(int, input().split())
divisors = enum_divisors(m)
divisors.reverse()
for g in divisors:
    if n <= m // g:
        print(g)
        break
