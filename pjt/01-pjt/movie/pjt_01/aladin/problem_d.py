import json


def best_book(books):
    id_lst = []
    for book in books:
        id_lst.append(book['id'])
    
    customerReviewRank_dict = {}
    customerReviewRank_lst = []
    for id in id_lst:
        book_json = open(f'C:/Users/SSAFY/Desktop/gs/PJT/01-pjt/movie/pjt_01/aladin/data/books/{id}.json', encoding='utf-8')
        book_list = json.load(book_json)
        # 여기서 평점은 가져올 수 있는데 평점이 가장 높은 타이틀을 어떻게 가져오냐
        customerReviewRank_dict[book_list['customerReviewRank']] = book_list['title']
        customerReviewRank_lst.append(book_list['customerReviewRank'])
    key = max(customerReviewRank_lst)
    bestbook = customerReviewRank_dict[key]
    
    return bestbook


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('C:/Users/SSAFY/Desktop/gs/PJT/01-pjt/movie/pjt_01/aladin/data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(best_book(books_list))