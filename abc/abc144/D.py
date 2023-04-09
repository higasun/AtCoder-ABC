import math

a, b, x = map(int, input().split())

half = a**2 * b / 2

if x >= half:
    # a * (a * a*tan(theta)) / 2 = v - x
    ans = math.atan((2.0*b - 2.0*x /(a**2))/a)
else:
    # (b * b / tan(theta))/2 * a = x -> tan(theta) = b**2 * a / 2
    ans = math.atan(b**2.0 * a / (2*x))
ans = math.degrees(ans)
print(ans)
