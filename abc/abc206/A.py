n = int(input())
n = int(n * 1.08)

thres = 206
if n < thres:
    print('Yay!')
elif n == thres:
    print('so-so')
else:
    print(':(')