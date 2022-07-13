from collections import deque

def solve(r):
    ans = 0
    for i in range(n):
        seen = [False]*n
        seen[i] = True
        que = deque(r[i])
        while que:
            new = que.popleft()
            seen[new] = True
            for x in r[new]:
                if not seen[x]:
                    que.append(x)
        
        ans += sum(seen)

    print(ans)

if __name__ == "__main__":
    n, m = map(int, input().split())

    if m > 0:
        r = [[] for _ in range(n)]
        for _ in range(m):
            a, b = map(int, input().split())
            r[a-1].append(b-1)
        solve(r)

    elif m == 0:
        print(n)