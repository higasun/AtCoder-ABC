from math import atan2, cos, sin

def same(p1, p2):
    if abs(p1[0] - p2[0]) < thres and abs(p1[1] - p2[1]) < thres:
        return True
    else:
        return False

def get_coordinates():
    gx, gy = 0, 0
    u = []
    for i in range(n):
        a, b = map(int, input().split())
        u.append((a, b))
        gx += a
        gy += b
    gx /= n
    gy /= n
    u = [(x-gx, y-gy) for x, y in u]

    return u

n = int(input())
thres = 1e-6

s = get_coordinates()
t = get_coordinates()

for i in range(n):
    if s[i][0] != 0 or s[i][1] != 0:
        s[0], s[i] = s[i], s[0]

ans = 'No'
for i in range(n):
    theta = atan2(t[i][1], t[i][0]) - atan2(s[0][1], s[0][0])

    rotated_s = [(cos(theta) * x - sin(theta) * y,
                    sin(theta) * x + cos(theta) * y) for x, y in s] 

    all_match = True
    for j in range(n):
        flg = False
        for k in range(n):
            if same(rotated_s[j], t[k]): 
                flg = True
        all_match &= flg
    
    if all_match: ans = 'Yes'

print(ans)