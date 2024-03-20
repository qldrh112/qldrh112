def sum_subset(i, len_subset, element_count, subtotal, target, elements):
    """
    params i: 부분 집합 원소의 인덱스(int)
    params len_bit: 부분집합 비트의 길이(int)
    params element_count: 부분 집합이 가져야 하는 원소의 수(int)
    params subtotal: i-1까지 고려한 합(int)
    params target: 부분 집합에서 찾고자 하는 원소의 합(int)
    params elements: 만든 부분 집합의 개수(int)
    return: element_count 개의 원소를 갖고 있는 원소의 합이 target 인 부분 집합의 여부 확인
    """
    global result
    global cnt
    cnt += 1

    # # 조기 종료 이거 끼면 왜 안 돌아갈까?
    # if result:
    #     return

    # 부분합이 목표에 도달하면, 원소의 개수를 검정하여 값을 반환합니다.
    if subtotal == target and element_count == elements:
        result += 1
        return

    # 부분집합의 원소를 더 이상 정할 수 없거나 선택한 원소가 규정된 원소보다 많을 때
    elif i == len_subset or element_count < elements:
        return

    # 이미 부분합이 목표를 초과하였을 때
    elif subtotal > target:
        return

    # 부분합에 나머지 원소를 다 더하여도 부분합에 도달하지 못할 때
    elif subtotal + sum(numbers[i:]) < target:
        return

    # 부분 집합의 원소를 정할 수 있고, 부분합이 목표를 초과하지 않았을 때
    else:
        sum_subset(i + 1, len_subset, element_count, subtotal + numbers[i], target, elements+1)
        sum_subset(i + 1, len_subset, element_count, subtotal, target, elements)


T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    numbers = list(range(1, 12 + 1))
    result = 0
    cnt = 0
    sum_subset(0, 12, N, 0, K, 0)
    # 출력합니다.
    print(f'#{t + 1} {result}')
    print(cnt)