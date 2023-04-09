n = int(input())
s = input()
is_altenate = True
for i in range(n-1):
    if s[i] == s[i+1]:
        is_altenate = False
        break
print('Yes' if is_altenate else 'No')
