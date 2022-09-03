x = int(input())

t = [0, 40, 70, 90]
for i in range(3):
    if t[i] <= x < t[i+1]:
        print(t[i+1] - x)
if 90 <= x:
    print('expert')