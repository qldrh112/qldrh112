def sorted_number(n, lst):
    """
    params n: 숫자 리스트의 길이 
    params lst: 숫자 리스트
    return: 오름차순으로 정렬된 숫자 리스트
    """
    # 특정 원소 인덱스의 +1과 비교할 것이므로 -1번 반복해줘야 한다.
    for i in range(n-1):              # 0, 1, 2, 3
        for j in range(n-i-1):        # 4, 3, 2, 1, 0
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    # return 위치 잘 잡을 것
    return lst

T = int(input())
for t in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    print(f'#{t+1}', *sorted_number(N, numbers))