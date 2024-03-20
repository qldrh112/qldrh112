import json
from pprint import pprint


def artist_info(artist, genres):
    artist_md = {
        'id' : artist['id'],
        'name': artist['name'],
        'type' : artist['type'],
        'images': artist['images'],
        'genres_names' : [x['name'] for x in genres if x['id'] in artist['genres_ids']],
    }
    return artist_md

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artist_json = open('C:/Users/SSAFY/Desktop/gs/PJT/01-pjt/movie/pjt_01/spotify/data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    genres_json = open('C:/Users/SSAFY/Desktop/gs/PJT/01-pjt/movie/pjt_01/spotify/data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artist_dict, genres_list))
