n, m = map(int, input().split())
student = []
for i in range(n):
    student.append(tuple(map(int, input().split())))
checkpoint = []
for i in range(m):
    checkpoint.append(tuple(map(int, input().split())))

for i in range(n):
    dist = float('inf')
    ans = -1
    a, b = student[i]
    for j in range(m):
        c, d = checkpoint[j]
        crr = abs(a-c) + abs(b-d)
        if crr < dist:
            ans = j+1
            dist = crr
    print(ans)
