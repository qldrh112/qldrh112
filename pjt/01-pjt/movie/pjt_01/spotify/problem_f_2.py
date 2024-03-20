"""
    장르에 acoustic이 포함된 아티스트 이름 목록 출력하기
"""

import json
from pprint import pprint


def acoustic_artists():
    output = []

    # 1
    genres_json = open(f'C:/Users/SSAFY/Desktop/gs/PJT/01-pjt/movie/pjt_01/spotify/data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    # 2
    for genre in genres_list:
        if genre['name'] == 'acoustic':
            acoustic_id = genre.get('id')
            break
    
    # 3
    artists_json = open('C:/Users/SSAFY/Desktop/gs/PJT/01-pjt/movie/pjt_01/spotify/data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    # 4
    for artist in artists_list:
        if acoustic_id in artist['genres_ids']:
            output.append(artist['name'])

    return output

# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    pprint(acoustic_artists())


"""
1. genres 파일 열기
2. 장르에서 acoustic 인 것 id 따오기
3. artists 파일 열기
4. 요소 하나씩 돌리면서 genres_ids에 어쿠스틱의 아이디가 포함되어 있으면 이름 리스트에 추가하기
"""