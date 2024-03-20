import json
from pprint import pprint


def artist_info(artists, genres):
    artists_md = []
    for artist in artists:
        artist_md = {
            'id' : artist.get('id'),
            'name' : artist.get('name'),
            'type' : artist.get('type'),
            'images': artist.get('images'),
            'genres_names' : [x['name'] for x in genres if x['id'] in artist['genres_ids']]
        }
        artists_md.append(artist_md)
    return artists_md


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open(f'C:/Users/SSAFY/Desktop/gs/PJT/01-pjt/movie/pjt_01/spotify/data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    genres_json = open('C:/Users/SSAFY/Desktop/gs/PJT/01-pjt/movie/pjt_01/spotify/data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artists_list, genres_list))
