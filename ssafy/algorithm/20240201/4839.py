def binary_search_count(P, to_search_page):
    """
    :param P: 전체 페이지 수
    :param return: 몇 번의 탐색을 수행하였는지
    몇 번의 이진 탐색으로 도착하는지
    """
    left = 1
    right = P
    count = 0

    while left <= right:
        count += 1
        mid = int((left + right) / 2)
        if mid == to_search_page:
            break
        elif mid > to_search_page:
            right = mid
        else:
            left = mid

    return count

T = int(input())
for t in range(T):
    P, Pa, Pb = map(int, input().split())

    # 횟수가 더 적은 사람을 출력합니다.
    if binary_search_count(P, Pa) < binary_search_count(P, Pb):
        print(f'#{t+1} A')
    elif binary_search_count(P, Pa) > binary_search_count(P, Pb):
        print(f'#{t+1} B')
    else:
        print(f'#{t+1} 0')
