import json


def best_new_books(books):
    # 초기 딕셔너리 이거를 for문 안에 집어넣어서 이 고생을 하네
    pubdate_2023 = {}
    # 2023년 출판 도서의 회원 리뷰 평점을 뽑습니다.
    for book in books:
        book_id = book.get('id')
        book_json = open(f'C:/Users/SSAFY/Desktop/gs/PJT/01-pjt/movie/pjt_01/aladin/data/books/{book_id}.json', encoding='utf-8')
        book_md = json.load(book_json)
        
        if book_md.get('pubDate')[:4] == '2023':
            # # key는 서명, value는 평점
            pubdate_2023.update({book_md['title'] : book_md['customerReviewRank']})

    #평점이 제일 높은 값을 찾고 해당 값을 가지고 있는 key 반환
    best_review_rank = max(pubdate_2023.values())

    for title in pubdate_2023:
        if pubdate_2023[title] == best_review_rank:
            best_new_book = title

    return best_new_book


        


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('C:/Users/SSAFY/Desktop/gs/PJT/01-pjt/movie/pjt_01/aladin/data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(best_new_books(books_list))
