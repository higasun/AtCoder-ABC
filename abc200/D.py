from collections import defaultdict


def solve(N):

    d = defaultdict(list)

    for bit in range(1, 2 ** N):
        x = 0
        for i in range(N):
            if (bit >> i) & 1:
                x += A[i] % 200

        d[x % 200].append(bit)


    for l in d.values():
        if len(l) > 1:
            print('Yes')

            # 数列B
            B = []
            bit = l[0]
            for i in range(N):
                if (bit >> i) & 1:
                    B.append(str(i+1))
            print(len(B), ' '.join(B))

            # 数列C
            C = []
            bit = l[1]
            for i in range(N):
                if (bit >> i) & 1:
                    C.append(str(i+1))
            print(len(C), ' '.join(C))

            return

    print('No')
    return 


if __name__ == "__main__":

    N = int(input())
    A = [int(x) for x in input().split()]
    
    N = min(N, 8)
    solve(N)