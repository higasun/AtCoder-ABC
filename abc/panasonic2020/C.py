a, b, c = map(int, input().split())
if pow((a + b - c), 2) > 4*a*b and c - a - b > 0:
    print('Yes')
else:
    print('No')