x, y, z = map(int, input().split())

if x > 0:
    if 0 < y and y < x and y < z:
        print(-1)
    elif z < 0 and 0 < y and y < x:
        print(abs(z)*2 + x)
    else:
        print(x)
else:
    if y < 0 and x < y and z < y:
        print(-1)
    elif z > 0 and x < y and y < 0:
        print(2 * z + abs(x))
    else:
        print(abs(x))