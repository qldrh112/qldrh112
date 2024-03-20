import sys
sys.stdin = open('input.txt', 'r')


def baby_gin():
    for i in range(6):
        player1[cards[2 * i]] += 1
        player2[cards[2 * i + 1]] += 1
        if i >= 2:
            # 중간에 run 이나 triplet 이 나오면 뽑은 순간 종료
            t_p1, t_p2 = triplet(player1, player2)
            r_p1, r_p2 = run1(player1, player2)

            if t_p1 or r_p1:
                return 1
            elif t_p2 or r_p2:
                return 2
    return 0


def run1(hands1, hands2):
    p1 = False
    p2 = False

    for i in range(10-2):
        if not p1 and hands1[i] > 0 and hands1[i + 1] > 0 and hands1[i + 2] > 0:
            p1 = True
        if not p2 and hands2[i] > 0 and hands2[i + 1] > 0 and hands2[i + 2] > 0:
            p2 = True

    return p1, p2


def triplet(hands1, hands2):
    p1 = False
    p2 = False

    for i in range(10 - 2):
        if not p1 and hands1[i] >= 3:
            p1 = True
        if not p2 and hands2[i] >= 3:
            p2 = True

    return p1, p2


T = int(input())
for t in range(T):
    cards = list(map(int, input().split()))
    # 카드 인덱스
    player1 = [0] * 10
    player2 = [0] * 10
    print(f'#{t+1} {baby_gin()}')