import urllib.request as ur
import urllib.parse as up
import http.cookiejar as hc
import re
#网站打开时会先生成一个cookies,里面只有csrfmiddlewaretoken值，需要把这个cookies保存下来，
#在登录的时候需要验证用到，还需要提取csrfmiddlewaretoken的值，在POST提交表单的时候
#需要提交三个数据，用户名、密码和该值，等验证登录通过以后，服务器会更新cookies,里面
#有两个值sessionid和csrfmiddlewaretoken，需要重新提取csrfmiddlewaretoken的值，因为已经
#发生变化了，然后再重新保存cookies到本地,后面的操作会一直用到这两项数据
url='http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex02/'
cookie=hc.MozillaCookieJar()
handler=ur.HTTPCookieProcessor(cookie)
opener=ur.build_opener(handler)
req=ur.Request(url)
res=opener.open(req)
#保存第一次cookies到本地
cookie.save('cookie.txt',ignore_discard=True, ignore_expires=True)
#提取csrfmiddlewaretoken值
for i in cookie:
    print(i)
    token=i.value
value={'csrfmiddlewaretoken':token,'username':'fangjun','password':'19870716'}
data=up.urlencode(value).encode('utf-8')
headers={
    "User-Agent":'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4',
    "referer":'http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex02/'
}
#加载cookies登录网站
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
handler=ur.HTTPCookieProcessor(cookie)
opener=ur.build_opener(handler)
#提交表单数据，这里的headers非必须项，仅作示例
req=ur.Request(url,data,headers)
res=opener.open(req)
#登录成功，重新保存cookies到本地
cookie.save('cookie.txt',ignore_discard=True, ignore_expires=True)
#测试密码开始
url='http://www.heibanke.com/lesson/crawler_ex02/'
#加载cookies
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
cookievalue=[]
for i in cookie:
    cookievalue.append(i.value)
#重新提取csrfmiddlewaretoken的值
token=cookievalue[0]
handler=ur.HTTPCookieProcessor(cookie)
opener=ur.build_opener(handler)
pat=re.compile(r'<h3>您输入的密码错误, 请重新输入</h3>')
for i in range(30):
    #还是需要提交三个数据
    data={'username':'xxx','password':i,'csrfmiddlewaretoken':token}
    data=up.urlencode(data).encode('utf-8')
    req=ur.Request(url,data)
    res=opener.open(req).read().decode('utf-8')
    if pat.search(res):
        print("it's wrong",i)
    else:
        print('right,the password is',i)
        break