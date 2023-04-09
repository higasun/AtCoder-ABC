import heapq

n, q = map(int, input().split())
called = []
heapq.heapify(called)
person = 0
gone = set()
for i in range(q):
    e = input().split()
    if e[0] == '1':
        heapq.heappush(called, person)
        person += 1
    elif e[0] == '2':
        x = int(e[1]) - 1
        gone.add(x)
    elif e[0] == '3':
        while called[0] in gone:
            heapq.heappop(called)
        print(called[0] + 1)
