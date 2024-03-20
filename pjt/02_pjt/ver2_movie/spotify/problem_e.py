import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def recommendation(track, artist, genre):
    """
    params track: 기준이 되는 노래
    params artist: 기준이 되는 아티스트
    params genre: 기준이 되는 장르
    return: 추천 노래 제목 목록(list) 
    """
    # 여기에 코드를 작성합니다.
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()

    # seed_track 파라미터
    params1 = {
        'q': track,
        'type':'track',
        'market': 'KR',
        'limit': 1,
    }
    # seed_artist 파라미터
    params2 = {
        'q': artist,
        'type': 'artist',
        'market': 'KR',
        'limit': 1,
    }
    
    # seed_track과 seed_artist 만들기
    track_responses = requests.get(f'{URL}/search', headers=headers, params=params1).json()
    seed_track = track_responses.get('tracks').get('items')[0].get('id')
    artist_responses = requests.get(f'{URL}/search', headers=headers, params=params2).json()
    seed_artist = artist_responses.get('artists').get('items')[0].get('id')

    # 추천 검색을 위한 새로운 파라미터
    params = {
        'seed_tracks': seed_track,
        'seed_artists': seed_artist,
        'seed_genres': genre,
        'market': 'KR',
    }

    # 새로운 검색과 결과 도출
    recommendation_responses = requests.get(f'{URL}/recommendations', headers=headers, params=params).json()
    result = [recommendation_responses['tracks'][i]['name'] for i in range(len(recommendation_responses['tracks']))]

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    주어진 트랙, 아티스트 이름, 장르로 음악 트랙 추천 목록 출력하기
    (주의) 요청마다 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('HypeBoy', 'BTS', 'acoustic'))
    # ['Best Of Me', 'A Drop in the Ocean', 'We Are', 'Dear Mr. President', 'Hurt']
