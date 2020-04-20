import pprint
import pandas as pd
import requests
from bs4 import BeautifulSoup



def scrapppping():
    url = "https://www.ambebi.ge/"
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    # print(soup)
    tags = soup.find_all('a')
    article_urls = []
    result = ''

    for tag in tags:
        a = str(tag.get('href'))
        if a.startswith('/article'):
            article_urls.append('https://www.ambebi.ge' + a)

    # pprint.pprint(article_urls)
    for url in article_urls:
        data = requests.get(url).text
        soup = BeautifulSoup(data, 'html.parser')
        article_block = soup.find_all('div', {'class': 'article_block'})
        # print(url)
        # print(article_block)

        for i in article_block:
            title = i.find('h1').text
            time = i.find('div').text
            content = i.find('div', {'class': 'article_content'}).text

        # print(title, '\n =  =  = ', content, '\n',
        #       '-------------------------------------------------------------', '\n')

        # print(title, '\n\n\n', content)
        result += title + '\n =  =  = ' + content + '\n-------------------------------------------------------------\n'

    return result

    # content = str(content).split()[0]


a = scrapppping()
