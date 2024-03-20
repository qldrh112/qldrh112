# n = 10
# queue = [0] * n
# front = rear = -1
#
# rear += 1
# queue[rear] = 10
# rear += 1
# queue[rear] = 20
# rear += 1
# queue[rear] = 30
#
# while front != rear:
#     front += 1
#     print(queue[front])

from collections import deque
deque1 = deque()
for i in range(1000000):
    deque1.append(i)
    print('밀어너엇')
print('append')

while deque1:
    deque1.popleft()
    print('아직이다 인마')
print('end')