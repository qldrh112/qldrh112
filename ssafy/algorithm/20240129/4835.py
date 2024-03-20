def prefix_sum(lst, list_length, prefix_length):
    """
    :param lst: 입력 리스트
    :param list_length: 리스트의 길이
    :param prefix_length: 부분합의 길이
    :return: 부분합 중 가장 큰 놈에서 작은 놈을 뺀 거

    전체 길이 - 부분합의 길이 + 1  => 계산해야 하는 마지막 부분합 인덱스
    리스트 표현식으로 lst[1] + lst[2] + lst[3] + ... 을 구현
    이것들을 합쳐서 prefix_list에 추가
    """
    prefix_list = []
    for i in range(list_length-prefix_length+1):
        prefix_list.append(sum([lst[i+x] for x in range(prefix_length)]))

    return max(prefix_list) - min(prefix_list)

T = int(input())                                    # 테스트 케이스의 수

for t in range(T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    print(f'#{t+1} {prefix_sum(lst, N, M)}')