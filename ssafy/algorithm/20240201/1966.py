def sort_num(N, lst):
    """
    :param N: 매개 변수 리스트의 길이
    :param lst: 정렬하고자 하는 숫자로 이루어진 리스트
    :return: 문자열로 정렬된 리스트를 반환
    리스트를 매개변수로 받아 선택 정렬을 통해 오름차순으로 정렬한 각 원소를 문자열로 반환하는 함수
    """
    for i in range(N-1):
        # 이번에 정렬할 인덱스
        min_idx = i
        # 자기 자신보다 더 큰 인덱스부터 검정
        for j in range(i+1, N):
            if lst[min_idx] > lst[j]:
                lst[min_idx], lst[j] = lst[j], lst[min_idx]
    return ' '.join(map(str, lst))

T = int(input())
for t in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    print(f'#{t+1} {sort_num(N, numbers)}')