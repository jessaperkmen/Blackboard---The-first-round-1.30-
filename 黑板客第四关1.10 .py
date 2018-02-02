import urllib.request as ur
import urllib.parse as up
import re
from http import cookiejar

n = 1
url_1 = 'http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex03/'
url_2 = 'http://www.heibanke.com/lesson/crawler_ex03/pw_list/?page=%d'%n
url_3 = 'http://www.heibanke.com/lesson/crawler_ex03/'
pwd_dict = {}
cookie = cookiejar.MozillaCookieJar()
handler = ur.HTTPCookieProcessor(cookie)
opener = ur.build_opener(handler)
content = opener.open(url_1)
cookie.save('cookies.txt',ignore_expires=True,ignore_discard=True)
print('首次cookies提取完成')
for i in cookie:
    token  = i.value
data = {'username':'z384478961',
        'password':'521125',
        'csrfmiddlewaretoken':token}
data = up.urlencode(data).encode('utf-8')
cookie.load('cookies.txt',ignore_discard=True,ignore_expires=True)
handler = ur.HTTPCookieProcessor(cookie)
opener = ur.build_opener(handler)
req = ur.Request(url_1,data)
content = opener.open(req)
cookie.save('cookies.txt',ignore_discard=True, ignore_expires=True)
print('cookies更新成功，开始爬取密码列表')
while n < 14:
    cookie.load('cookies.txt',ignore_discard=True,ignore_expires=True)
    handler = ur.HTTPCookieProcessor(cookie)
    opener = ur.build_opener(handler)
    req = ur.Request(url_2)
    content = opener.open(req).read().decode('utf-8')
    pattern = re.compile('title="password_pos">(.*?)</td>.*?<td.*?title="password_val">(.*?)</td>',re.S|re.M)
    items = re.findall(pattern,content)
    for i in items:
        if i in pwd_dict:
            continue
        else:
            pwd_dict[i[0]] = i[1]
    print('第%d页完成，开始下一页'%n)
    n += 1
    if len(pwd_dict) < 100:
        if n >13 :
            print('有缺项,继续')
            print('当前长度为%d'%len(pwd_dict))
            n = 1
        else:
            continue
    else:
        break

dict = sorted(pwd_dict.items(),key = lambda x : int(x[0]))
print(len(dict))
print(dict)
print('密码是：')
for i in dict:
    print(i[1], end="")

