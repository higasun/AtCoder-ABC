N = int(input())
count = 0
for a in range(1, N+1):
    if a*a*a > N: break
    for b in range(a, N+1):
        if a*b*b>N: break
        count += N//(a*b) - (b-1)
print(count)