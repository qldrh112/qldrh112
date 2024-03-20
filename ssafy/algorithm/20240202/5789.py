def box_number_change(N, Q, lst):
    """
    :param N: 상자의 개수
    :param Q: 변경 개수
    :param lst: 변경 사항(리스트)
    :return: 상자에 적힌 숫자
    """

    box = [0] * N
    for i in range(Q):
        # 첫 번째 상자는 인덱스가 0이므로 1을 빼줘야 한다.
        for j in range((lst[i][0])-1, lst[i][1]):
            # i가 원래 0부터 시작하므로 1을 더해줘야 한다.
            box[j] = i+1

    return box

T = int(input())
for t in range(T):
    N, Q = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(Q)]
    # 출력합니다.
    print(f'#{t+1}', *box_number_change(N, Q, lst))