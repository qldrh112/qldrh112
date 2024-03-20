from urllib import response
import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def get_related_artists(name):
    """
    params name: 아티스트의 이름(str)
    return: 연관된 아티스트의 이름 목록(list)
    """
    # 여기에 코드를 작성합니다.
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    params = {
        'q': name,
        'type': 'artist',
    }
    """
    responses: 입력받은 아티스트를 검색어로 한 일반 검색 결과
    id: 입력받은 아티스트의 고유 번호
    related_artists: 입력받은 아티스트와 관련한 아티스트들의 정보
    result: 연관된 아티스트의 이름 리스트
    """
    responses = requests.get(f'{URL}/search', headers=headers, params=params).json()
    id = responses.get('artists').get('items')[0].get('id')
    related_artists = requests.get(f'{URL}/artists/{id}/related-artists', headers=headers).json()
    result = [related_artists['artists'][i]['name'] for i in range(len(related_artists['artists']))]
    
    # 빈 리스트(연관된 artist가 없다) -> None 반환
    if result:
        return result
    else:
        return None

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    아티스트가 존재하면 해당 아티스트의 id를 기반으로 연관 아티스트 목록 구성
    아티스트가 없을 경우 None을 반환
    (주의) 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(get_related_artists("NewJeans"))
    # ['STAYC', 'NMIXX', 'LE SSERAFIM', 'IVE', ... 생략 ..., 'CHUNG HA']

    pprint(get_related_artists("OldShirts"))
    # None
