import json


def sorted_cs_books_by_price(books, categories):

    # 컴퓨터 공학의 고유번호 따오기
    for category in categories:
        if category.get('name') ==  '컴퓨터 공학':
            computer_science_code = category.get('id')

    # 카테고리가 컴퓨터 공학인 도서의 제목과 카테고리 떼오기
    computer_science_books = {}
    for book in books:
        if computer_science_code in book['categoryId']:
            computer_science_books[book['title']] = book['priceSales']

    cs_books = []
    # sorted는 리스트를 정렬하고 반환하는 함수
    orderby_price = sorted(list(computer_science_books.values()), reverse=True)

    # 판매 가격이 높은 순서대로 제목을 정렬하기
    for price in orderby_price:
        for title in computer_science_books:
            if computer_science_books[title] == price:
                cs_books.append(title)

    return cs_books 



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('C:/Users/SSAFY/Desktop/gs/PJT/01-pjt/movie/pjt_01/aladin/data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('C:/Users/SSAFY/Desktop/gs/PJT/01-pjt/movie/pjt_01/aladin/data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    print(sorted_cs_books_by_price(books, categories_list))
