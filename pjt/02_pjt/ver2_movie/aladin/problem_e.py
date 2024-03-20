from turtle import bk
import requests
from pprint import pprint


def ebook_list(title):
    """
    params title: 도서명
    return: 전자 도서의 isbn,  itemid, link, pricesales
    종이 서적의 판매가보다 10% 이상 저렴한 전자 도서의 정보를 반환하는 함수
    """
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
    params = {
        'TTBkey': 'key',
        'Query': title,
        'QueryType': 'Title',
        'SearchTarget': 'eBook',
        'Output': 'JS',
        'Version': '20131101',
    }
    # 입력받은 제목의 ebook 목록
    ebook_response_js = requests.get(URL, params=params).json()['item']

    fir_bk_price = bk_price(title)
    if fir_bk_price == None:
        return None
    
    bk_info = []

    for i in range(len(ebook_response_js)):
        if ebook_response_js[i]['priceSales'] * 1.1 < fir_bk_price:
            bk_info_dict = {
                'isbn': ebook_response_js[i]['isbn'],
                'itemId': ebook_response_js[i]['itemId'],
                'link': ebook_response_js[i]['link'],
                'priceSales': ebook_response_js[i]['priceSales'],
            }
            bk_info.append(bk_info_dict)

    return bk_info

def bk_price(title):
    """
    params title: 도서명
    return: 도서 가격
    서명을 입력받아 첫번째 검색된 도서(종이로 된)의 판매가를 반환합니다.
    """
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
    params = {
        'TTBkey': 'ttbdidie85200114001',
        'Query': title,
        'QueryType': 'Title',
        'Output': 'JS',
        'Version': '20131101',
    }

    # 첫번째 검색 도서의 가격 정보
    try:
        fir_bk_price = requests.get(URL, params=params).json()['item'][0]['priceSales']
    except IndexError:
        return None
    
    return fir_bk_price

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(ebook_list('베니스의 상인'))

    pprint(ebook_list('*'))
