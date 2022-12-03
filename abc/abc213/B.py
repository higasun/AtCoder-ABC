n = int(input())
a = [(i, int(x)) for i, x in enumerate(input().split(), 1)]
a.sort(key=lambda x: x[1])
print(a[-2][0])