def baking_pizza(fire_pit_volumes, pizza, cheese):
    """
    fire_pit: 화덕
    fire_pit_volumes: 화덕에 들어가 수 있는 피자의 수(int)
    pizza: 피자의 수(int)
    cheese: 각 피자의 치즈 양(list)
    return: 화덕에 가장 마지막까지 남아있는 피자 번호(int)
    """
    # 순환큐는 필요한 양보다 하나 더 만듭니다.
    fire_pit = [0] * (fire_pit_volumes + 1)
    # cheese 의 인덱스
    i = 0
    front = rear = 0

    # 초기값 입력
    for _ in range(fire_pit_volumes):
        fire_pit[rear+1] = i
        rear += 1
        i += 1

    output = -1
    # 큐를 소진했다면
    while front != rear:
        front = (front + 1) % (fire_pit_volumes + 1)
        output = fire_pit[front]
        cheese[output] //= 2

        # 치즈가 남아있으면
        if cheese[output] > 0:
            rear = (rear + 1) % (fire_pit_volumes + 1)
            fire_pit[rear] = output

        # 치즈가 떨어졌고 넣을 피자가 있다면
        elif i < pizza:
            rear = (rear + 1) % (fire_pit_volumes + 1)
            fire_pit[rear] = i
            i += 1

        # 치즈가 떨어졌는데 넣을 게 없다면 rear 를 늘리지 못한다.

    return output+1

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    # 출력합니다.
    print(f'#{t + 1} {baking_pizza(N, M, Ci)}')