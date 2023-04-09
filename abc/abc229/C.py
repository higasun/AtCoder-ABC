n, w = map(int, input().split())
pizza = []
for i in range(n):
    p = tuple(map(int, input().split()))
    pizza.append(p)
pizza.sort(reverse=True)

taste = 0
idx = 0
while w > 0 and idx < n:
    a, b = pizza[idx]
    crr_w = min(w, b)
    taste += a * crr_w
    
    w -= crr_w
    idx += 1
print(taste)
