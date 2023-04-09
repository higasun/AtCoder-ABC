s = input()
l = len(s)
for i in range(2, l, 2):
    mid = (l-i) // 2
    if s[:mid] == s[mid:l-i]:
        print(l - i)
        break
