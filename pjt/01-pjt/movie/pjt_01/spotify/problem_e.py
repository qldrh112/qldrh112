import json
from pprint import pprint

def dec_artists(artists):
    # 1
    output = []
    for artist in artists:
        id = artist.get('id')
        artist_json = open(f'C:/Users/SSAFY/Desktop/gs/PJT/01-pjt/movie/pjt_01/spotify/data/artists/{id}.json', encoding='utf-8') 
        artist_dict = json.load(artist_json)

    # 2
        # 리스트를 자를 수 없다.
        if artist_dict['followers']['total'] > 10000000:
            name_uri_id_dict = {
                'name' : artist_dict['name'],
                'uri_id' : artist_dict['uri'].split(':')[-1]
            }
            output.append(name_uri_id_dict)

    return output
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('C:/Users/SSAFY/Desktop/gs/PJT/01-pjt/movie/pjt_01/spotify/data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    pprint(dec_artists(artists_list))


"""
팔로워 수를 이용하여 모든 아티스트 중 팔로워 수의 총합이 10,000,000 이상인 아티스트의 정보를 리스트로 출력하는 알고리즘 작성
1. artists에서 id따서 id.json 열기
2. followers 딕셔너리 안에 있는 total > 10,000,000 인 것의 이름과 uri-id를 가져온다.
"""