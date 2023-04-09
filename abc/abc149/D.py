N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

winning_hand = {'r': 'p', 's': 'r', 'p': 's'}
hand = [winning_hand[op_hand] for op_hand in T]
point = {'r': R, 's': S, 'p': P}

def wins(x, y):
    return x == winning_hand[y]

total = 0
for i in range(K):
    while i < N:
        if i - K >= 0 and hand[i-K] == hand[i]:
            hand[i] = 'o'
        if wins(hand[i], T[i]):
            total += point[hand[i]]
        i += K
print(total)