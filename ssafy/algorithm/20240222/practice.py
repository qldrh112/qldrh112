"""
숫자 하나를 입력받아 2 x 7 행렬에 
첫번째 열: 행이 하나씩 우측으로 갈수록 N을 하나씩 증가시켜 [0:4]까지 입력
두번째 열: 행이 하나씩 좌측으로 갈수록 N을 하나씩 감소시켜 [6:2]까지 입력
"""
"""
파일로 두 수를 입력받아 그것의 합과 곱을 계산하여 output.txt에 입력하는 함수
"""
# import sys
#
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')
#
# n1, n2 = map(int, input().split())
# print(n1 + n2)
# print(n1 * n2)

# N = int(input())
# arr = [[0] * 7 for _ in range(2)]
#
# for i in range(2):
#     num = N
#     for j in range(4):
#         if i == 0:
#             arr[i][j] = num
#             num += 1
#         else:
#             arr[i][-1-j] = num
#             num -= 1
# print(arr)

# 16진수를 2진수로 바꾸는 함수
input_data = input()
binary = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
output = ''
for i in range(2, len(input_data)):
    output += binary[int(input_data[i])]

print(output)