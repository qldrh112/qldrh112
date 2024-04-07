from collections import deque
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

def f():
    results = []
    window = deque()
    max_v = float('-inf')

    for i, v in enumerate(nums):
        window.append(v)
        # window에 k개 만큼 요소가 쌓여야 하므로
        if i < k - 1:
            continue
        
        # 슬라이스 윈도우 안의 최대값 교체
        if max_v == float('-inf'):
            max_v = max(window)
        elif max_v < v:
            max_v = v
        
        results.append(max_v)

        if max_v == window.popleft:
            max_v = float('-inf')
    
    return results

print(f())