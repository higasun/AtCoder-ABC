a, b, c = map(int, input().split())

if c % 2 == 0:
    if abs(a) < abs(b): flg = 1
    elif abs(a) > abs(b): flg = -1
    else: flg = 0
else:
    if a < b: flg = 1
    elif a > b: flg = -1
    else : flg = 0

if flg == 1:
    print('<')
elif flg == -1:
    print('>')
else:
    print('=')