a, b = map(int, input().split())
if b == 0:
    ans = 'Gold'
elif a == 0:
    ans = 'Silver'
else: 
    ans = 'Alloy'
print(ans)
