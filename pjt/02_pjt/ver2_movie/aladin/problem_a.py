from encodings import search_function
import json
import requests

def author_works():
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

    # parameter를 저장합니다.
    params = {
        'TTBkey' : 'key',
        'Query' : '파울로 코엘료',
        'MaxResults' : 20,
        'QueryType' : 'Author',
        'Output' : 'JS',
        'Version' : '20131101',
    }

    # API를 통한 응답을 가져옵니다.
    response = requests.get(URL, params=params)
    response_json = response.json()['item']

    # 필요한 리스트인 제목만 가져옵니다.
    title_list = [response_json[i]['title'] for i in range(len(response_json))]
    return title_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(author_works())
