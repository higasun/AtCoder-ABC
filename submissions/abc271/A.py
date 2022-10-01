n = int(input())

d = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

res = ""
q = n // 16
r = n % 16
if q >= 1:
    if 10 <= q:
        res += d[q]
    else:
        res += str(q)
    
    if 10 <= r:
        res += d[r]
    else:
        res += str(r)
    
else:
    if 10 <= r:
        res = "0" + d[r]
    else:
        res = "0" + str(r)

print(res)