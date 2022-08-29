a = input()
x = a[:-2]
y = int(a[-1])
if 0 <= y <= 2:
    print(x+"-")
elif 3 <= y <= 6:
    print(x)
elif 7 <= y <= 9:
    print(x+"+")