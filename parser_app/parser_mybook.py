
import requests
from bs4 import BeautifulSoup as BS4

URL = 'https://mybook.ru/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request

def get_data(html):
    bs = BS4(html, features='html.parser')
    items = bs.find_all('div', class_='e4xwgl-0 iJwsmp')
    mybook_list = []
    for item in items:
        title = item.find('p', class_='lnjchu-1 hhskLb').get_text(strip=True)
        author = item.find('div', class_='dey4wx-1 jVKkXg').get_text(strip=True)
        description = item.find('p', class_='lnjchu-1 dPgoNf').get_text(strip=True)
        rating = item.find('div', class_='sc-1vvnv6o-0 hRWuUu sc-1v96hyo-1 bNNLDW').get_text(strip=True)
        mybook_list.append(
            {
                'title': title,
                'author': author,
                'description': description,
                'rating': rating
            }
        )
    return mybook_list

def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        book_list = []
        for page in range(1, 2):
            response = get_html("https://mybook.ru/catalog/books/", params={"page": page})
            book_list.extend(get_data(response.text))
        return book_list
    else:
        raise Exception("error")

print(parsing())
