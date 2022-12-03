A = [int(x) for x in input().split()]
A = sorted(A)

flg = (A[1] - A[0] == A[2] - A[1])
print('Yes' if flg else 'No')