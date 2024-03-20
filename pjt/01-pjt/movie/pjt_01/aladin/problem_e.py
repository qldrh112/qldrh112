import json


def new_books(books):
    # 여기에 코드를 작성합니다.
    bk_id_lst = []
    for book in books:
        bk_id_lst.append(book['id'])
    
    # 추출한 id를 기반으로 상세 페이지를 엽니다.
    pubdate_dict = {}
    for id in bk_id_lst:
        book_json = open(f'C:/Users/SSAFY/Desktop/gs/PJT/01-pjt/movie/pjt_01/aladin/data/books/{id}.json', encoding='utf-8')
        md_dict = json.load(book_json)

        # 개별 책의 메타데이터에서 서명을 key로 발행일을 value로 넣습니다.
        pubdate_dict[md_dict['title']] = md_dict.get('pubDate')
    
    # 출판연도가 2023년인 도서를 리스트로
    output = []
    for key, value in list(pubdate_dict.items()):
        if value[:4] == '2023':
            output.append(key)

    return output



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('C:/Users/SSAFY/Desktop/gs/PJT/01-pjt/movie/pjt_01/aladin/data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(new_books(books_list))