import requests
from pprint import pprint


def author_other_works(title):
    """
    param title: 표제
    return: 입력받은 책의 저자의 다른 저작물
    """
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

    params = {
        'TTBkey' : 'key',
        'Query' : title,
        'Output' : 'JS',
        'Version' : '20131101',
    }

    # 검색 결과에서 저자를 뽑습니다.
    try:
        response = requests.get(URL, params=params).json()['item'][0]['author']
        author = response.split(',')
        response1 = requests.get(URL, params=params).json()
    except IndexError:
        return None
    
    # 서명(저자 역할어)에서 서명을 뽑아내기 
    for i in range(len(author[0])):
        if author[0][i] == '(':
            author_name = author[0][:i-1]
            break

    return  author_works(author_name)


def author_works(first_author):
    """
    param first_author: 제1저자
    return: 입력받은 책의 저자의 다른 저작물
    """
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

    # parameter를 저장합니다.
    params = {
        'TTBkey' : 'ttbdidie85200114001',
        'Query' : first_author,
        'MaxResults' : 20,
        'QueryType' : 'Author',
        'Output' : 'JS',
        'Version' : '20131101',
    }

    # API를 통한 응답을 가져옵니다.
    response = requests.get(URL, params=params).json()['item']
    
    # 필요한 리스트인 제목만 반환합니다.
    return [response[i]['title'] for i in range(len(response)) if i < 5]


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(author_other_works('베니스의 상인'))

    pprint(author_other_works('개미'))

    pprint(author_other_works('*'))
