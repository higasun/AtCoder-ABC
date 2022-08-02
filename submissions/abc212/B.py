x = input()
mod = 10
ans = 'Strong'
if x[0] == x[1] == x[2] == x[3]:
    ans = 'Weak'

cnt = 0
for i in range(3):
    if (int(x[i]) + 1)%mod == int(x[i+1]):
        cnt += 1
if cnt == 3: ans ='Weak'

print(ans)