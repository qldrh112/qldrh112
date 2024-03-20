def create_cyphers(nums):
    """
    nums: 8자리의 암호(list)
    return: 만들어진 암호
    """
    # 8자리, 8자리로 나누어 사이클을 돌린다.
    queue = [1] * 16
    front = rear = 0

    # 초기값 넣기
    for i in range(8):
        queue[rear] = nums[i]
        rear += 1

    while queue[rear] > 0:
        for j in range(1, 5+1):

            # 암호의 자리값이 0보다 크면
            if queue[front] - j > 0:
                queue[rear] = queue[front] - j
                front = (front + 1) % 16
                rear = (rear + 1) % 16

            # 작으면 끝을 0으로 바꾸고 for j 종료
            else:
                queue[rear] = 0
                break
    
    # front 가 rear 보다 뒤에 있으면
    if front >= rear:
        return queue[front + 1:] + queue[:rear + 1]
    # front 가 rear 보다 앞에 있으면
    else:
        return queue[front + 1 : rear + 1]


for _ in range(10):
    t = int(input())
    input_nums = list(map(int, input().split()))
    # 출력합니다.
    print(f'#{t}', *create_cyphers(input_nums))