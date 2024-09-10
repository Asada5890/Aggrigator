from bs4 import BeautifulSoup
import requests
from models import Article

def parser_fun():
    response = requests.get('https://habr.com/ru/rss/all/')
    soup = BeautifulSoup(response.content, 'xml')
    items = soup.find_all('item')
    for item in items:
        title = item.find('title').text
        link = item.find('link').text
        description = item.find('description').text
        if not Article.objects.filter(link=link).exists():
            # If not, create a new Article object
            Article.objects.create(title=title, link=link, description=description)
            print(f'Added new article: {title}')
        else:
            print(f'Article already exists: {title}')