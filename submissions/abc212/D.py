import heapq

q = int(input())
a = []
diff = 0

for _ in range(q):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        x = query[1]
        heapq.heappush(a, x-diff)
    elif query[0] == 2:
        x = query[1]
        diff += x
    else:
        print(heapq.heappop(a)+diff)

