from math import cos, sin, atan2

def coordinates(n):
    a, b = [], []
    gx = 0
    gy = 0
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
        gx += x
        gy += y
    gx /= n
    gy /= n
    for i in range(n):
        a[i] -= gx
        b[i] -= gy
    
    return a, b

def solve(a, b, c, d, n):

    eps = 1e-6
    ans = 'No'

    for i in range(n):
        if a[i] != 0 or b[i] != 0:
            tmp = a[i], b[i]
            a[i], b[i] = a[0], b[0]
            a[0], b[0] = tmp
    
    for i in range(n):
        flag = True
        theta = atan2(d[i], c[i]) - atan2(b[0], a[0])
        for j in range(n):
            A = a[j]*cos(theta) - b[j]*sin(theta)
            B = a[j]*sin(theta) + b[j]*cos(theta)
            flag2 = False
            for k in range(n):
                if abs(A - c[k]) < eps and abs(B - d[k]) < eps: flag2 = True
            flag &= flag2
        
        if flag: ans = 'Yes'

    return ans

def main():
    n = int(input())
    a, b = coordinates(n)
    c, d = coordinates(n)
    ans = solve(a, b, c, d, n)
    print(ans)

if __name__ == "__main__":
    main()