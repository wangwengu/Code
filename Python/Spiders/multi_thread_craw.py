import requests
from scrapy import Selector
from urllib.parse import urljoin

def catch_chapter():
    url = 'https://www.booktxt.net/8_8455/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    res = requests.get(url, headers = headers).content.decode('gbk')
    response = Selector(text = res)
    chapter_url_list = response.xpath('//div[@id="list"]//dd/a/@href').getall()
    for i in range(len(chapter_url_list)):
        chapter_url_list[i] = urljoin(url, chapter_url_list[i])
    chapter_url_list = chapter_url_list[6:-4]
    print(chapter_url_list)

def save_chapter():
    pass

if __name__ == '__main__':
    catch_chapter()