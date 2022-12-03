p = [int(x)-1 for x in input().split()]
a = 'abcdefghijklmnopqrstuvwxyz'

res = [a[x] for x in p]
print(''.join(res))