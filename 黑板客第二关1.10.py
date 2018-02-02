import urllib.request
import re
n = 0
url = 'http://www.heibanke.com/lesson/crawler_ex01/'
data = {'csrfmiddlewaretoken':'QMw1AeoJzyYzRtd0WTEQM1qdfY4fcmhj',
'username':'sdfasdfa',
'password':str(n)}
pattern = re.compile('<h3>(.*?)</h3>')
i ='您输入的密码错误, 请重新输入'
while True:
    data = {'csrfmiddlewaretoken': 'QMw1AeoJzyYzRtd0WTEQM1qdfY4fcmhj',
            'username': 'sdfasdfa',
            'password': str(n)}
    data = urllib.parse.urlencode(data).encode('utf-8')
    res = urllib.request.Request(url,data = data)
    req = urllib.request.urlopen(res).read()
    content = req.decode('utf-8')
    item = re.findall(pattern,content)
    if i in item :
        n += 1
    else :
        print('h3 内容改变')
        print(data)
        break



