import json
from pprint import pprint


def book_info(book, categories_list):
    md = {
        'author': book['author'],
        'categoryName': '',
        'cover': book['cover'],
        'description' : book['description'],
        'id' : book['id'],
        'priceSales' : book['priceSales'],
    }
    categoryId = book['categoryId'] #[123,1324]
    categorynamelst = []
    for subject in categories_list:
        if subject['id'] in categoryId:
            categorynamelst.append(subject['name'])
    md['categoryName'] = categorynamelst
    return md


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))
