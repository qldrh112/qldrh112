# def push(item, size):
#     global top
#     top += 1
#     if top == size:
#         print('overflow!')
#     else:
#         stack[top] = item
#
# size = 10
# stack = [0] * size
# top = -1
#
# push(10, size)
#
# def pop():
#     global top
#     if top == -1:
#         print('underflow!')
#         return 0
#     else:
#         top -= 1
#         return stack[top+1]
#
# print(pop())
#
# if top > -1: # pop()
#     top -= 1
#     print(stack[top+1])


# def push(n):
#     global top
#     top += 1
#     if top == 10:
#         print('Overflow!')
#     else:
#         stack[top] = n
#
#
# top = -1
# stack = [0] * 10        # 최대 10개 push 가능
#
# top += 1                # push(10)
# stack[top] = 10
# top += 1                # push(20)
# stack[top] = 20
#
# push(30)
#
# while top >= 0:
#     print(stack[top])
#     top -= 1


# '''
# 2
# (()))
# '''
#
# def f1(c, d):
#     e = c + d
#     return f2(e)
#
# def f2(n):
#     n *= 2
#
#     return n
#
# a = 10
# b = 20
# c = a + b
# print(f1(a, b))

# def f(i, k):         # i: 현재 위치, k: 목표
#     if i == k:
#         print(brr)
#     else:
#         brr[i] = arr[i]
#         f(i+1, k)
#
# arr = [10, 20, 30]
# N = len(arr)
# brr = [0] * N
# f(0, N)


"""
memo를 위한 배열을 할당하고 모두 0으로 초기화한다.
memo[0]을 0으로 memo[1]은 1로 초기화한다.
"""

def fibo1(n):
    global memo


def fibo(n):
    global cnt
    cnt += 1
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

def fibo_memo(n):
    global count
    count += 1
    if n != 0 and memo[n] == 0:
        memo[n] = fibo_memo(n-1) + fibo_memo(n-2)
    return memo[n]



cnt = 0
count = 0
n = 7
print(f'피보나치수열의 {n}번째 자리는: {fibo(7)}')
print('count: ', cnt)

memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1
print(fibo_memo(n), count)
print(memo)