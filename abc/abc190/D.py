n = int(input())
m = 2*n

count = 0
for i in range(1, int(m**0.5)+1):
    if m % i == 0 and (i % 2) != (m//i % 2): count += 2
print(count)