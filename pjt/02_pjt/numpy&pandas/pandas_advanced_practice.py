import numpy as np
import pandas as pd

# pandas로 csv 읽어오기
df = pd.read_csv('C:/Users/SSAFY/Desktop/gs/PJT/02-pjt/numpy&pandas/data/test_data.CSV', encoding='cp949')
print(df.head())

"""
parse_dates: 열 이름을 넣어주면 데이터 타입을 datatime64[ns]로 변환해준다.
pd.to_datetime() 함수로 datetime64로 바꿀 수도 있다.
'2019-01-01 같은 스트링 형태의 자료형을 datetime64로 바꿀 수 있다.

usecols: 여러 열 중 필요한 열만 가져온다.
"""
df = pd.read_csv('C:/Users/SSAFY/Desktop/gs/PJT/02-pjt/numpy&pandas/data/test_data.CSV', encoding='cp949', usecols=['이름', '나이'])
print(df.head())

# nrows: 파일의 처음 n개의 행을 읽는다. 데이터 세트가 매우 큰 경우 유용하다.
df = pd.read_csv('C:/Users/SSAFY/Desktop/gs/PJT/02-pjt/numpy&pandas/data/test_data.CSV', encoding='cp949', nrows=10)
print(df.shape)         # (10, 5)

print(df)
"""
    이름  나이 성별    직업    사는곳
0  서팔광  25  남    교수   경상남도
1  황지필  28  여    군인   경상북도
2  김일제  36  남    기자  서울/경기
3  곽마권  34  남   리포터    강원도
4  마풍강  45  남    모델    강원도
5  김덕협  67  여   개발자  서울/경기
6  나대물  32  여   카텐더   충청북도
7  유덕창  24  남  학원강사   전라북도
8  황충유  34  여   개발자    강원도
9  가원창  54  남    화가   충청북도
"""

# value_counts
# 기본 함수에도 있던 함수, 범주형 열의 값 분포를 확인하는 데 유용
# 발생 횟수와 함께 열의 고유 값을 반환
df = pd.read_csv('C:/Users/SSAFY/Desktop/gs/PJT/02-pjt/numpy&pandas/data/test_data.CSV', encoding='cp949')
print(df['성별'].value_counts())
"""
성별
남    26
여    24
Name: count, dtype: int64
"""
""" '성별'은 따로 지정도 안 해줬는데 출력이 되네 참 편리하군"""

# 분포를 비율로 확인하기
print(df['성별'].value_counts(normalize=True))
"""
성별
남    0.52
여    0.48
Name: proportion, dtype: float64
"""

# astype
# 데이터 분석 전 데이터 타입을 적절한 것으로 변환하는 것은 필수
# 함수는 특정 데이터 타입만 받거나 특정 데이터 타입을 효율적으로 돌리기 때문이다.
df ['이름'] = df['이름'].astype(str)        # 왜 df[이름] = df[이름]을 먹인거지?
print(df.dtypes)                            # str은 object 라고 한다.
"""
이름     object
나이      int64
성별     object
직업     object
사는곳    object
dtype: object
"""

# 여러 열의 데이터 타입 한 번에 변경하기
df = df.astype({'성별': 'category', '직업': 'str'})
print(df.dtypes)
"""
이름       object
나이        int64
성별     category
직업       object
사는곳      object
dtype: object
"""

# isna & notna
# na = numpy의 Na(not a number)을 의미함
# 데이터에 결측값이 존재하는 경우 존재
df = pd.read_csv('C:/Users/SSAFY/Desktop/gs/PJT/02-pjt/numpy&pandas/data/test_data_has_null.CSV', encoding='cp949')
print(df.head())
"""
    이름    나이 성별   직업    사는곳
0  서팔광  25.0  남   교수   경상남도
1  황지필  28.0  여   군인   경상북도
2  김일제  36.0  남  NaN  서울/경기
3  곽마권  34.0  남  리포터    강원도
4  마풍강  45.0  남   모델    강원도
"""

# isna 은 결측값이면 True, 정상값이면 False
# notna의 경우 결측값이면 false, 정상 값이면 True(무한 값(np.inf)나 띄어쓰기' '는 결측값으로 판단하지 않는다.)
# isna
print(df.head().isna())
"""
      이름     나이     성별     직업    사는곳
0  False  False  False  False  False
1  False  False  False  False  False
2  False  False  False   True  False
3  False  False  False  False  False
4  False  False  False  False  False
"""
""" 왜 사는 곳은 검사가 되지 않을까? """

# notna
print(df.head().notna())
"""
     이름    나이    성별     직업   사는곳
0  True  True  True   True  True
1  True  True  True   True  True
2  True  True  True  False  True
3  True  True  True   True  True
4  True  True  True   True  True
"""

#누락된 값의 수 구하기
print(df.isna().sum())
"""
이름     0
나이     5
성별     1
직업     5
사는곳    2
dtype: int64
"""

# 행 별로 누락된 값의 수 구하기
print(df.isna().sum(axis=1))       # axis = 0 or index: 결측값이 있는 행 삭제, axis = 1 or columns: 결측값이 있는 열을 삭제
"""
0     0
1     0
2     1
3     0
4     0
이하생략
"""

# isnull() vs isna()
# 동일한 함수, db에서 온 양반들을 위해 isnull을 새로 만들어주었다.
""" 당연히 isnull()을 아니 쓸 수가 없겠네요 """

# 결측치를 처리하는 방법
# 1. 버리기
# 2. 채우기

# dropna
df = pd.read_csv('C:/Users/SSAFY/Desktop/gs/PJT/02-pjt/numpy&pandas/data/test_data_has_null.CSV', encoding='cp949')
print(df.isna().sum())   

# dropna는 dataframe을 반환한다.
# 원본 dataframe을 변경하고 싶으면 inplace=True를 설정해준다.

df.dropna(axis=0, inplace=True) # 결측값이 있는 행을 날려라
print(df.isna().sum())
"""
이름     0
나이     0
성별     0
직업     0
사는곳    0
dtype: int64
"""

# how
# any: row 또는 column에 NaN 값이 하나만 있어도 drop -> default
# all: row 또는 column에 모든 값이 NaN 이어야 drop

df = pd.read_csv('C:/Users/SSAFY/Desktop/gs/PJT/02-pjt/numpy&pandas/data/test_data_has_null.CSV', encoding='cp949')
df.dropna(axis=0, how='all', inplace=True)
print(df.isna().sum())
"""
이름     0
나이     5
성별     1
직업     5
사는곳    2
dtype: int64
"""
""" 아마도 짐작컨대 모든 값이 null인 것이 없으니까 dropna 명령을 수행하지 않은 것이라고 볼 수 있다."""

df = pd.read_csv('C:/Users/SSAFY/Desktop/gs/PJT/02-pjt/numpy&pandas/data/test_data_has_null.CSV', encoding='cp949')
df.dropna(axis=0, how='any', inplace=True)
print(df.isna().sum())
"""
이름     0
나이     0
성별     0
직업     0
사는곳    0
dtype: int64
"""

# thresh
# 결측값이 아닌 열이 몇 개 이상일 경우, 삭제하지 않겠다는 임계치를 설정한다.
# axis = 0, thresh=3 일 때, 결측값이 아닌 열이 3개 이상이면 삭제하지 않는다.
df = pd.read_csv('C:/Users/SSAFY/Desktop/gs/PJT/02-pjt/numpy&pandas/data/test_data_has_null.CSV', encoding='cp949')
df.dropna(axis=0, thresh=4, inplace=True) # 원본에 있는 null 값을 날려라, 근데 결측값이 아닌 열이 4개 이상이면 삭제하지 않는다.
print(df.isna().sum())
"""
이름     0
나이     4
성별     1
직업     4
사는곳    2
dtype: int64
"""

# fillna 결측값을 다른 적절한 값으로 채워준다.
df['직업'].fillna('무직', inplace=True)
print(df.head())
"""
    이름    나이 성별   직업    사는곳
0  서팔광  25.0  남   교수   경상남도
1  황지필  28.0  여   군인   경상북도
2  김일제  36.0  남   무직  서울/경기
3  곽마권  34.0  남  리포터    강원도
4  마풍강  45.0  남   모델    강원도
"""
""" 점점 전에 배운 것이 흐릿해진다."""

print(df.isna().sum())
"""
이름     0
나이     4
성별     1
직업     0 -> null 값 다 날라갔네?
사는곳    2
dtype: int64
"""

# groupby
# 열의 고유한 값을 기반으로 행을 그룹화한다.
# 독립된 그룹에 대하여 별도로 데이터를 처리하거나 그룹별 통계량을 확인하고자 할 때 유용하다.
# groupby는 아래 3단계로 이루어져 있다.
# 1. split: 정의한 컬럼 조건에 따라 독립된 그룹으로 나누는 단계
# 2. apply: sub-group에 그룹별 함수를 적용하는 단계
# 3. combine: 각 sub-group 별로 함수가 적용된 결과를 종합하여 다시 하나의 테이블로 합침

# 직업 별 평균 나이 구하기
df = pd.read_csv('C:/Users/SSAFY/Desktop/gs/PJT/02-pjt/numpy&pandas/data/test_data_has_null.CSV', encoding='cp949')
print(df.groupby('직업').mean(numeric_only = True))   # 같은 직업을 가진 양반들끼리 나누기 -> mean이 평균이라는 뜻이 있다. -> 통합
"""
            나이
직업
감정평가사    35.00
개발자      45.60
건축가      26.00
검사       15.00
게임기획자    78.00
교수       25.00
군인       28.00
이하 생략
"""

""" 대단하군 """

# 직업 별 평균 나이에서 성별을 추가적으로 구분하여 출력하는 예시 코드
print(df.groupby(['직업', '성별']).mean(numeric_only=True).reset_index())  # reset index()는 그럼 2개 이상의 칼럼이 들어가면 반드시 써야 하는 것인가?
"""
         직업 성별         나이
0     감정평가사  남  35.000000
1       개발자  남  50.666667
2       개발자  여  43.428571
3       건축가  남  25.000000
4        검사  남  15.000000
5        검사  여        NaN
6     게임기획자  여  78.000000
7        교수  남  25.000000
이하 생략
"""

# unique & nunique
# unique: 고유값의 종류를 모두 출력
print(df['직업'].unique())
"""
['교수' '군인' nan '리포터' '모델' '개발자' '학원강사' '화가' '변호사' '법무사' '판사' '검사' '미술가'
 '게임기획자' '프로게이머' '감정평가사' '빅데이터전문가' '대학교수' '대역배우' '도어맨' '패션모델' '휴대폰디자이너'
 '웹디자이너' '웹개발자' '건축가']
 """

# nunique: 고유값의 개수를 반환
print(df['나이'].nunique())             # 29

# 정렬
# 정렬의 기준은 오름차순이다.
print(df['이름'].sort_values())
"""
9     가원창
11    계식도
3     곽마권
28    구동범
18    권필쌍
40    금땡구
이하 생략
"""

# 내림차순은 ascending=False 옵션을 추가해준다.
print(df['이름'].sort_values(ascending=False))
"""
8     황충유
1     황지필
30    홍혁팔
26    홍학철
23    허태유
37    허곽의
이하 생략
"""

# 모든 컬럼을 보기 위해서는 by 옵션을 활용할 것
print(df.sort_values(by=['나이']))
"""
     이름    나이   성별       직업    사는곳
19  방신마  15.0    남       검사  서울/경기
30  홍혁팔  17.0    남  빅데이터전문가   전라북도
10  마석대  23.0    여     학원강사   경상북도
41  김꽃길  23.0    여      개발자    강원도
7   유덕창  24.0    남     학원강사   전라북도
16  배용팔  25.0    남       판사   경상북도
이하 생략"""

"""이건 select * 하고 order by로 해놓은 거랑 같네"""

# 두 가지 이상의 정렬
# 직업 별 오름차순, 나이 별 내림차순
print(df.sort_values(by=['직업', '나이'],ascending=[True, False]))
"""
     이름    나이   성별       직업    사는곳
28  구동범  35.0    남    감정평가사   경상북도
5   김덕협  67.0    여      개발자  서울/경기
29  금천규  67.0    여      개발자    제주도
12  최덕복  64.0    남      개발자    강원도
27  문태범  45.0    남      개발자    제주도
22  엄석용  43.0    여      개발자   전라남도
이하 생략
"""

""" 우선 직업이 오름차순으로 갈기고, 직업이 같으면 내림차순으로 해라"""

