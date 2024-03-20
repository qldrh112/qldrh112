import json
from pprint import pprint


def books_info(books, categories):
    md_lst = []
    for book in books:
        md = {
            'author': book['author'],
            'categoryName': '',
            'cover': book['cover'],
            'description' : book['description'],
            'id' : book['id'],
            'priceSales' : book['priceSales'],
            'title' : book['title'],
            }
        categorynamelst = []
        categoryid = book['categoryId']

        for subject in categories:
            if subject['id'] in categoryid:
                categorynamelst.append(subject['name'])

        md['categoryName'] = categorynamelst
        md_lst.append(md)
    return md_lst



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))