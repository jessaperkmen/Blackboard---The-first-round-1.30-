#-*- encoding:utf-8 -*-
import requests
import re
n = 43295
while True:
    try:
        url = 'http://www.heibanke.com/lesson/crawler_ex00/%d/'%int(n)
        print(url)
        data = requests.get(url)
        pattern = re.compile('<h3>.*?数字是(.*?)\..*?',re.S|re.M)
        content = re.findall(pattern,data.text)
        n = content[0]
        print('代码为',n)
    except:
        url = 'http://www.heibanke.com/lesson/crawler_ex00/%s/' % n
        data = requests.get(url)
        print('网页已到尽头！')
        print(data.text)
        break





