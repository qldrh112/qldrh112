def counting_sort(lst):
    """
    :param lst: 매개 변수로 받은 리스트
    :return: 오름차순으로 정렬된 리스트
    리스트를 받아 카운팅 정렬 기법으로 오름차순으로 정렬하여 반환하는 함수
    """
    sorted_list = [0] * len(lst)        # 정렬된 리스트
    counts = [0] * (len(lst)+1)         # 리스트 각 요소의 누적합을 나타낸 리스트

    for i in range(0, len(lst)):
        counts[lst[i]] += 1

    for i in range(1, len(lst)+1):
        counts[i] += counts[i-1]

    for i in range(len(sorted_list)-1, -1, -1):
        counts[lst[i]] -= 1
        sorted_list[counts[lst[i]]] = lst[i]

    return sorted_list


def flatten(dump, arr):
    """
    :param dump: 옮길 수 있는 횟수
    :param arr: 상자가 쌓여 있는 높이를 나타낸 리스트
    :return: 가장 높이 쌓은 상자와 가장 낮게 쌓은 상자의 높이 차
    dump가 0이 될 때까지 가장 높게 쌓은 상자에서 가장 낮게 쌓은 상자로 옮깁니다.
    옮길 때마다 상자를 다시 정렬합니다.
    """
    arr = counting_sort(arr)
    while dump > 0:
        # 평탄화가 완료되면 평탄화된 높이를 반환합니다.
        if arr[0] == arr[-1]:
            return arr[0]

        dump -= 1
        arr[-1] -= 1
        arr[0] += 1

        arr = counting_sort(arr)
    return arr[-1] - arr[0]


for t in range(10):
    dump = int(input())
    input1 = list(map(int, input().split()))
    print(f'#{t+1} {flatten(dump, input1)}')