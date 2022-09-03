n = int(input())
s = [list(input()) for _ in range(n)]
t = [list(input()) for _ in range(n)]

def rot(s):
    return list(zip(*s[::-1]))

def find_left_top(s):
    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                return i, j

def is_same(s, t):
    si, sj = find_left_top(s)
    ti, tj = find_left_top(t)

    offset_i, offset_j = ti - si, tj - sj

    for i in range(n):
        for j in range(n):
            ii, jj = i + offset_i, j + offset_j
            if 0 <= ii <= n-1 and 0 <= jj <= n-1:
                if s[i][j] != t[ii][jj]:
                    return False
            else:
                if s[i][j] == '#':
                    return False
    
    return True

cnt_s = sum([1 for i in range(n) for j in range(n) if s[i][j]=='#'])
cnt_t = sum([1 for i in range(n) for j in range(n) if t[i][j]=='#'])
if cnt_s != cnt_t:
    print('No')
    exit()


for _ in range(4):
    if is_same(s, t):
        print('Yes')
        exit()
    s = rot(s)

print('No')