n, m = map(int, input().split())

s = (n % 12) * 30 + m / 2
l = 6 * m

diff = min(abs(s-l), 360-abs(s-l))
print(diff)
