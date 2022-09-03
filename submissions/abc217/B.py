d = {'ABC': False, 'ARC': False, 'AGC': False, 'AHC': False}
for _ in range(3):
    s = input()
    d[s] = True

for k, b in d.items():
    if not b:
        print(k)