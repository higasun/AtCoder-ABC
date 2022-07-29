n = int(input())
s = input()
for i, c in enumerate(s):
    if c == '1':
        if i % 2 == 0:
            print('Takahashi')
        else:
            print('Aoki')
        break