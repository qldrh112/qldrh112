import requests
from pprint import pprint


def best_review_books():
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

    params = {
        'TTBkey' : 'key',
        'Query' : '파울로 코엘료',
        'QueryType' : 'Author',
        'MaxResult' : '20',
        'Output' : 'JS',
        'Version' : '20131101',
    }

    # API를 통해 필요한 정보를 가져옵니다.
    response = requests.get(URL, params=params)
    response_json = response.json()['item']
    
    # 고객 평점이 9점이 넘는 작품을 가져옵니다.
    best_review_books = [response_json[i] for i in range(len(response_json)) if response_json[i]['customerReviewRank'] >= 9]

    return best_review_books

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(best_review_books())
