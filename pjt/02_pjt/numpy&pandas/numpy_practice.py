# 필요 패키지 import
import csv 
import numpy as np
import pandas as pd
from pprint import pprint 

"""
csv, json 등 특정 파일 확장자를 다루는 것이 python에는 내장되어 있구나 역시
"""

# 기존 배열을 numpy array로 변형
arr = [30123, 431409, 49041304, 43143, 56456]
np_arr = np.array(arr)
print(np_arr)           # [   30123   431409 49041304    43143    56456]
print(type(np_arr))     # <class 'numpy.ndarray'>

# 기본 배열 생성
arr = np.arange(15)
print(arr)              # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]


# arange는 range() 함수의 구성요소와 동일하게 사용 가능하다.
arr = np.arange(5, 15, 3)
print(arr)              # [ 5  8 11 14]

"""
뭔가 배열이 띄어쓰기가 제각각인 거 같냐?
"""


# Numpy 2차원 배열 생성
# reshape(row, column)
#arr = np.arange(10).reshape(2, 3) # 1차원 배열을 2행 3열로 만들어라
#print(arr)                         # ValueError
# reshape의 인자의 곱이 배열의 개수와 맞지 않으면 에러가 발생한다. 

arr = np.arange(10).reshape(2, 5)
print(arr) 
"""
[[0 1 2 3 4]
 [5 6 7 8 9]]
 """

arr = np.arange(12).reshape(2, 3, 2)
print(arr)
"""
[[[ 0  1]
  [ 2  3]
  [ 4  5]]

 [[ 6  7]
  [ 8  9]
  [10 11]]]
"""

"""이렇게 말도 안 되게 배열의 크기를 크게 만들어버릴 수 있다."""


# 0으로만 이루어진 배열 생성
# np.zeros((row, column), dtype=데이터 타입)
arr = np.zeros((3, 4), dtype=np.int64)
print(arr)
"""
[[0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]]
"""

# Numpy는 반드시 (행, 축)의 형태로 인자를 받는 모습을 볼 수 있다.

# 요소가 1로 이루어진 배열 생성
# np.ones(row, column), dtype=데이터 타입) 사용
arr = np.ones((2, 3), dtype=np.int64)
print(arr)
"""
[[1 1 1]
 [1 1 1]]
 """

# 특정 문자나 수로 이루어진 배열 생성
# np.full((row, column), 값) 사용
arr = np.full((5, 5), '응')
print(arr)
"""
[['응' '응' '응' '응' '응']
 ['응' '응' '응' '응' '응']
 ['응' '응' '응' '응' '응']
 ['응' '응' '응' '응' '응']
 ['응' '응' '응' '응' '응']]
 """

# 균일한 간격의 숫자 생성
# 주로 그래프의 x축을 그릴 때 많이 사용한다.
# lin은 선형 간격 값을 생성하는 것을 나타냄 -> 로그 간격 값을 생성하는 logspace와 대조 됨
# np.linspace(구간 시작점, 구간 끝점, 구간 내 숫자 개수)활용
arr = np.linspace(0, 10, 5)                   # 2단위로 자르겠다는 거임
print(arr)
# [ 0.   2.5  5.   7.5 10. ]

""" 아니네 0부터 10까지 숫자 5개니까 양끝점 제외하고, 3개로 0~10을 나눠먹는 거네 """

# 랜덤한 값 생성
# np.random.rand(생성하고자 하는 숫자의 수) 활용
arr = np.random.rand(5) 
print(arr)
# [0.67637555 0.48915015 0.83646391 0.83788214 0.11703636]
# [0.03017311 0.60931058 0.2636851  0.34193169 0.33762429]
""" import 로 랜덤을 안 땡겨와도 되는 거였어?"""

# 2차원 배열로 생성
# np.random.rand(x축 개수, y축 개수)
arr = np.random.rand(2, 3)
print(arr)
"""
[[0.60083804 0.12441165 0.7471687 ]
 [0.15532787 0.58306603 0.65202713]]
 """

# 원하는 범위 내의 정수 값을 원하는 개수로 생성하기
# np.random.randint(범위, size=개수)
arr = np.random.randint(4, size=10)
print(arr)
# [3 2 1 2 1 1 0 3 3 3]

# 기본 함수
arr = np.arange(15).reshape(5, 3)

# 배열 각 축(axis)의 크기
print(arr.shape)           # (5, 3)

# 축의 개수(차원, Dimension)
print(arr.ndim)            # 2

# 각 요소(Element)의 타입
print(arr.dtype)        # dtype('int32')

""" 이거 각 요소가 다 다르면 어떻게 표기되지? """

# 각 요소(Element)의 타입의 bytes의 크기
print(arr.itemsize)     # 4 

""" 32bit = 4bytes라? """

# 전체 요소의 개수
print(arr.size)         # 15

# 인덱싱
arr = np.arange(16).reshape(4, 4)

print(arr[1][2])           # 6 (2행의 3열)
print(arr[1, 2])           # 6 (2행의 3열)


# 슬라이싱
# 리스트에서 2차원 배열 슬라이싱은 다음과 같이 진행된다.
# 2행 이후의 것을 3열까지 따와라
arr = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]
print([arr[:3] for arr in arr[2:]])                 # [[10, 11, 12], [15, 16, 17], [20, 21, 22]]

"""우선 이런 방법이 가능한 지도 몰랐다. 참으로 놀라운 일이다."""

# Numpy 에서는 이것이 이렇게 가능하다.
# 1번행 이상 / 3번행 미만, 2번 열 미만 출력
arr = np.arange(25).reshape(5, 5)
print(arr[1:3, : 2])
"""
[[ 5  6]
 [10 11]]
 """

# 배열 값 수정 & 복사하기
# index 접근 후 수정은 python 일반형과 동일
# 그냥 값만 따오면 얕은 복사 발생
# 깊은 복사를 위해서는 np.copy() 사용할 것

# 얕은 복사
arr = np.arange(4).reshape(2, 2)
arr2 = arr
arr2[0][0] = 5
print(arr)
"""
[[5 1]
 [2 3]]
 """

# 깊은 복사
arr = np.arange(9).reshape(3, 3)
arr2 = np.copy(arr)
arr2[0, 0] = 10
print(arr)
"""
[[0 1 2]
 [3 4 5]
 [6 7 8]]
"""



