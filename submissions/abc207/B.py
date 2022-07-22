import math
a, b, c, d = map(int, input().split())

if b >= d*c:
    print(-1)
else:
    print(math.ceil(a  / (d*c - b)))

"""
A,B,C,D = map(int,input().split())
ans = -1
diff = C*D-B
if 0 < diff:
    ans = (A+diff-1)//diff
print(ans)
"""