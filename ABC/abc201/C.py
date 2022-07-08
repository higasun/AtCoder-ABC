S = input()
in_list, out_list = [], []
for i, s in enumerate(S):
    if s == 'o':
        in_list.append(i)
    elif s == 'x':
        out_list.append(i)

cnt = 0
for i in range(10000):
    p = list(int(x) for x in str(i).zfill(4))
    password = set(p)

    flg = True
    for j in in_list:
        if not j in password:
            flg = False
            break
    
    for j in out_list:
        if j in password:
            flg = False
            break

    if flg: cnt += 1

print(cnt)