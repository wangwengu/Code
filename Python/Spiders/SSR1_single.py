# 单线程爬取

import json
import time

import requests
from scrapy import Selector

total_movie = 0
total_succeed_movie = 0
total_fail_movie = 0

def get_page(page):
    base_url = 'https://ssr1.scrape.center/page/%s'
    global total_movie, total_succeed_movie, total_fail_movie
    data = []
    url = base_url % page
    print(url)
    html = requests.get(url).text
    response = Selector(text = html)
    movie_basic_info_selector_list = response.xpath('//div[@class="el-card item m-t is-hover-shadow"]')
    fail_movie = 0
    movie_basic_info_selector_list_len = len(movie_basic_info_selector_list)
    for j in range(movie_basic_info_selector_list_len):
        title = movie_basic_info_selector_list[j].css('.m-b-sm::text').getall()
        tags = movie_basic_info_selector_list[j].css('.categories span::text').getall()
        area = movie_basic_info_selector_list[j].xpath('.//div[@class="m-v-sm info"][1]/span[1]/text()').getall()
        movie_duration = movie_basic_info_selector_list[j].xpath('.//div[@class="m-v-sm info"][1]/span[3]/text()').getall()
        era = movie_basic_info_selector_list[j].xpath('.//div[@class="m-v-sm info"][2]/span/text()').getall()
        score = movie_basic_info_selector_list[j].xpath('normalize-space(.//p[@class="score m-t-md m-b-n-sm"]/text())').getall()
        img = movie_basic_info_selector_list[j].css('.cover::attr(src)').getall()
        detail_url = movie_basic_info_selector_list[j].xpath('.//img[@class="cover"]/../@href').getall()
        movie_basic_info_dist = {'title': title, 'tags': tags, 'area': area, 'time': movie_duration, 'era': era, 'score': score, 'img': img, 'detail_url': detail_url, 'detail_url_info': None}
        try:
            movie_basic_info_dist['detail_url_info'] = get_detail_url('https://ssr1.scrape.center%s' % detail_url[0])
            data.append(movie_basic_info_dist)
            print('第%d页的第%d部电影详情页抓取成功' % (page, j + 1))
        except Exception as e:
            print('第%d页的第%d部电影详情页抓取失败' % (page, j + 1))
            k = 1
            while k <= 5:
                try:
                    print('正在尝试第%d次重新抓取' % k)
                    movie_basic_info_dist['detail_url_info'] = get_detail_url('https://ssr1.scrape.center%s' % detail_url[0])
                    data.append(movie_basic_info_dist)
                    break
                except Exception as e:
                    print('第%d次重新抓取失败' % k)
                    print(e)
                k += 1
            if k > 5:
                print('第%d页的第%d部电影详情页重新抓取失败' % (page, j + 1))
                fail_movie += 1
            else:
                print('第%d页的第%d部电影详情页重新抓取成功' % (page, j + 1))
    total_movie += movie_basic_info_selector_list_len
    total_succeed_movie += movie_basic_info_selector_list_len - fail_movie
    total_fail_movie += fail_movie
    print('第%d页抓取完毕，共抓取%d部电影，成功%d部电影，失败%d部电影' % (page, movie_basic_info_selector_list_len, movie_basic_info_selector_list_len - fail_movie, fail_movie))
    return data

def get_detail_url(url):
    print(url)
    html = requests.get(url).text
    response = Selector(text = html)
    data = []
    intro = response.xpath('normalize-space(//div[@class="drama"]/p/text())').getall()
    intro_dist = {'intro': intro}
    data.append(intro_dist)
    director_name = response.xpath('//div[@class="el-row"][2]//p[@class="name text-center m-b-none m-t-xs"]/text()').getall()
    director_img = response.xpath('//div[@class="el-row"][2]//img[@class="image"]/@src').getall()
    director_dist = {'name': director_name, 'img': director_img}
    director_info = {'director_info': director_dist}
    data.append(director_info)
    actor_selector_list = response.xpath('//div[@class="actor el-col el-col-4"]')
    actor_list = []
    for actor_selector in actor_selector_list:
        actor_name = actor_selector.xpath('.//p[@class="el-tooltip name text-center m-b-none m-t-xs item"]/text()').getall()
        actor_role = actor_selector.xpath('.//p[@class="el-tooltip role text-center m-b-none m-t-xs item"]/text()').getall()
        actor_img = actor_selector.xpath('.//img[@class="image"]/@src').getall()
        actor_dist = {'actor_name': actor_name, 'actor_role': actor_role, 'actor_img': actor_img}
        actor_list.append(actor_dist)
    actor_info = {'actor_info': actor_list}
    data.append(actor_info)
    photo_selector_list = response.xpath('//div[@class="photo el-col el-col-3"]')
    photo_list = []
    for photo_selector in photo_selector_list:
        img = photo_selector.xpath('.//img[@class="el-image__inner el-image__preview"]/@src').getall()
        img_dist = {'img': img}
        photo_list.append(img_dist)
    photo_info = {'photo_info': photo_list}
    data.append(photo_info)
    return data

def save_data(data):
    try:
        with open('./SSR1.json', 'a', encoding = 'UTF-8') as fp:
            fp.write(json.dumps(data, indent = 4, ensure_ascii = False) + '\n')
            print('写入成功')
    except Exception as e:
        print('写入失败')
        print(e)

def run(page):
    data = []
    for i in range(1, page + 1):
        print('正在抓取第%d页电影' % i)
        try:
            data.append(get_page(i))
            print('第%d页电影抓取成功' % i)
        except:
            print('第%d页电影抓取失败' % i)
            k = 1
            while k <= 5:
                print('正在尝试第%d次重新抓取' % k)
                try:
                    data.append(get_page(i))
                    print('第%d次重新抓取成功' % k)
                    break
                except:
                    print('第%d次重新抓取失败' % k)
                k += 1
    save_data(data)
    print('共抓取%d部电影，成功%d部电影，失败%d部电影' % (total_movie, total_succeed_movie, total_fail_movie))

if __name__ == '__main__':
    start = time.time()
    run(10)
    end = time.time()
    print('程序运行时间大约为：%d秒，合计%d分钟' % (int(end - start), (int((end - start + 59) / 60))))