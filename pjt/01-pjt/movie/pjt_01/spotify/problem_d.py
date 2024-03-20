import json


def max_polularity(artists):
    # 1
    popularity_dict = {}
    for artist in artists:
        id = artist.get('id')
        artist_json = open(f'C:/Users/SSAFY/Desktop/gs/PJT/01-pjt/movie/pjt_01/spotify/data/artists/{id}.json', encoding="utf-8")
        artist_list = json.load(artist_json)

    # 2
        # 딕셔너리에 요소 추가할 때는 update로 해라
        popularity_dict.update({artist['name'] : artist_list['popularity']})

    # 3
    max_popularity = max(list(popularity_dict.values()))

    # 4
    # key를 가져와서 dict[key] = value로 비교하면 key 값 따기 가능
    for name in popularity_dict:
        if popularity_dict[name] == max_popularity:
            return name




# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    artists_json = open('C:/Users/SSAFY/Desktop/gs/PJT/01-pjt/movie/pjt_01/spotify/data/artists.json', encoding="utf-8")
    artists_list = json.load(artists_json)

    print(max_polularity(artists_list))


# 모든 아티스트 중 가장 높은 인기도를 가진 아티스트를 출력하는 알고리즘

# 1. artists에서 for로 돌려서 id를 따서 각각의 정보가 담긴 json을 연다.
# 2. key를 이름 value를 popularity로 따온다.
# 3. values()로 값 리스트 따와서 max()함수로 하나 뽑아놓는다.
# 4. 이름-평점쌍 딕셔너리로 이름을 돌렸을 때, 제일 높은 평점을 가진 이름이 나오면 반환한다.