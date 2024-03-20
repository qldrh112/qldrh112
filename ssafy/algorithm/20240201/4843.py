def special_sort(N, lst):
    """
    :param N: 입력받은 리스트의 길이
    :param lst: 정렬하고자 하는 리스트
    :return: 정렬된 리스트
    리스트를 인자로 받아 규칙에 따라서 정렬하고 반환하는 함수
    """
    # 10개짜리 리스트이므로
    sorted_lst = [0] * 10

    # 오름차순 정렬
    for i in range(N-1):
        min_value_idx = i
        for j in range(i+1, N):
            if lst[min_value_idx] > lst[j]:
                lst[min_value_idx], lst[j] = lst[j], lst[min_value_idx]

    # 맨 뒤, 맨 앞 순서로 번갈아가며 재배열한다.
    for i in range(10):
        if i % 2 == 0:
            sorted_lst[i] = lst.pop(-1)
        else:
            sorted_lst[i] = lst.pop(0)

    return sorted_lst

T = int(input())
for t in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    # 출력합니다.
    print(f'#{t+1}', *special_sort(N, numbers))