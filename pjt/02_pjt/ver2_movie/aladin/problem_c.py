import requests
from pprint import pprint


def bestseller_book():
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

    params = {
        'TTBkey' : 'key',
        'Query' : '파울로 코엘료',
        'QueryType' : 'Author',
        'Sort' : 'SalesPoint',
        'Output' : 'JS',
        'Version' : '20131101',
    }

    # salespoint 기준으로 정렬된 도서 정보 딕셔너리를 가져옵니다.
    response = requests.get(URL, params=params).json()['item']

    # 상위 5개의 salepoint 도서의 제목을 가져옵니다.
    return [response[i]['title'] for i in range(5)]

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(bestseller_book())
