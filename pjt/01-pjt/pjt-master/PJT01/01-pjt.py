# 내 코드에 다른 패키지를 추가
import requests
import pprint

API_key = 'key'

# 서울의 위도
lat = 37.56
# 서울의 경도
lon = 126.97

# https://openweathermap.org/current
url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'

# 해당 url으로부터 json형태로 가져온다.
data = requests.get(url).json()
# pprint.pprint(data['weather'])

# 날씨 요약 정보: 서울 기준 'clear sky'가 출력되도록 하자!
pprint.pprint(data['weather'][0]['description'])

# 추가 공부 과제
'''
data['weather']
data.get('weather')

이거 두 개 차이가 뭐냐?
전자는 key가 'weather'인 것을 가져오는 것이고
후자는 value가 'weather'인 것을 가져오는 것
'''

