# coding：utf-8
import requests
from lxml import etree

# import re
#
# pattern = re.compile(r'<a.*?href="(.*?)".*?title="(.*?)".*?>')
# resp = requests.get('https://s.weibo.com/top/summary')
# if resp.status_code == 200:
#     all_match = pattern.findall(resp.text)
#     for href, title in all_match:
#         print(href)
#         print(title)

for page in range(1, 11):
    resp = requests.get(url=f'https://movie.douban.com/top250?start={(page - 1) * 25}',
                        headers={'user-Agent': 'BaiduSpider'})
    # print(resp.text)
    tree = etree.HTML(resp.text)
    titles = tree.xpath(f'/html/body/div[3]/div[1]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]')
    rates = tree.xpath(f'/html/body/div[3]/div[1]/div/div[1]/ol/li[1]/div/div[2]/div[2]/div/span[2]')
    for title, rate in zip(titles, rates):
        print(title.text, rate.text)
