def queue_rotation(n, do, queue):
    """
    n: 수열의 크기(int)
    do: 작업 횟수(int)
    queue: 수열(1차원 list)
    return: 작업을 do번 했을 때, 맨 앞의 있는 숫자
    """
    front = 0
    rear = -2

    # 원형 큐
    for _ in range(do):
        queue[(rear+1) % n] = queue[front]
        front = (front+1) % n

    return queue[front]

T = int(input())
for t in range(T):
    N, M = map(int, input().split())    # 3 10
    input_nums = list(map(int, input().split())) # 5527 731 31274
    print(f'#{t+1} {queue_rotation(N, M, input_nums + [0])}')