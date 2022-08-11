ans = "AC"
t = "Hello,World!"
s = input()

if len(s) != len(t):
    ans = "WA"
else:
    for i in range(len(s)):
        if s[i] != t[i]:
            ans = "WA"
print(ans)