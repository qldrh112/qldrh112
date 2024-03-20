"""
    팔로워가 5,000,000이상, 10,000,000미만인 아티스트들을 
    아티스트 이름과 팔로워를 목록으로 출력하기
"""

import json
from pprint import pprint


def get_popular():
    # 1
    output = []
    
    artists_json = open('C:/Users/SSAFY/Desktop/gs/PJT/01-pjt/movie/pjt_01/spotify/data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)
   
    # 2
    

    for artist in artists_list:
        id = artist['id']
        artist_md_json = open(f'C:/Users/SSAFY/Desktop/gs/PJT/01-pjt/movie/pjt_01/spotify/data/artists/{id}.json', encoding="utf-8")
        artist_md = json.load(artist_md_json)

        # 3 # {'followers': dd, 'name' : ddd} 뭔가 더 맛있게 짜는 방법이 없을까?
        if 5000000 <= artist_md['followers']['total'] < 10000000:
            name_follower_dict = {
                'followers' : artist_md['followers']['total'],
                'name' : artist_md['name']
            }
            output.append(name_follower_dict)

    return output


# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    pprint(get_popular())


"""
1. 전체 리스트 따놓기, artists.json 열기
2. 1에서 딴 아티스트의 id로 개별 아티스트.json 파일 열기
3. 5,000,000 <= follower - total < 10,000,000 인 거 {name:follower}형식으로 list에 추가
"""