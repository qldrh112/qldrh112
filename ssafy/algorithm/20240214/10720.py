def touramant_game(left, right):
    if left == right:
        print('같다', left, right)
        return left
    else:
        print('left 이전: left, right')
        left = touramant_game(left, (left+right)//2)
        print('left 이후: left, right')
        right = touramant_game((left+right)//2+1, right)
        return sho_bu(left, right)


def sho_bu(i, j):
    # 무승부는 앞선 사람이 먹는다.
    print('쇼부다', j, i)
    if cards[j] - cards[i] == 1 or cards[j] - cards[i] == -2:
        return j
    else:
        return i


T = int(input())
for t in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
    print(f'#{t+1} {touramant_game(0, N-1)+1}')


def win(a, b):
    # 가위1 바위2 보3 2>1, 3>2, 1>3
    print('쇼부다', b, a)
    if card[b] - card[a] == 1 or card[b] - card[a] == -2:  # 승자b
        return b
    else:
        return a


def f(i, j):  # i~j번 사이 승자를 리턴하는 함수
    if i == j:  # 한명인 경우 부전승
        print('같다', i, j)
        return i
    else:
        print('left 이전: left, right')
        left = f(i, (i + j) // 2)
        print('left 이후: left, right')
        right = f((i + j) // 2 + 1, j)
        return win(left, right)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 학생수, 1~N번까지
    card = list(map(int, input().split()))
    print(f'#{tc} {f(0, N - 1) + 1}')