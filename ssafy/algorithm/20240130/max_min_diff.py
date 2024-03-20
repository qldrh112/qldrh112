def max_min_diff(N, arr):
    """
    :param N: 양수 리스트의 길이
    :param arr: N개의 양수 리스트
    :return: 최대값과 최소값 사이의 거리

    인자로 받은 숫자 리스트를 순회하며 가장 큰 값과 그 인덱스, 가장 작은 값과 인덱스를 찾고,
    그 인덱스 간 차를 반환하는 함수
    """

    max_value_idx = 0
    min_value_idx = 0

    for i in range(N):
        if arr[max_value_idx] <= arr[i]:        # 같은 값도, max_value를 변경할 수 있게 해줘야 마지막에 나온 색인을 참고
            max_value_idx = i+1

        if arr[min_value_idx] > arr[i]:
            min_value_idx = i+1             # 문제에서 요구하는 인덱스는 1부터니까

    if max_value_idx - min_value_idx > 0:
        return max_value_idx - min_value_idx
    else:
        return min_value_idx - max_value_idx

T = int(input())
for t in range(T):
    N = int(input())
    input1 = list(map(int, input().split()))            # [1, 1, 2, 3, 3]
    print(f'#{t+1} {max_min_diff(N, input1)}')
