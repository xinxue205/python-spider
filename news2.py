import urllib.request
import re

pat = r'<a.*?href="(.*?)".*?>(.*?)</a>'


def isInfo(content, surl):
    if re.match( r'http://finance.sina.com.cn/zl/', surl, re.M|re.I): return 0
    if re.match( r'http://blog.sina.com.cn/', surl, re.M|re.I): return 0
    return 1

url = "https://finance.sina.com.cn/"
#伪装浏览器用户
headers = {'User-Agent':'User-Agent:Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'}
req = urllib.request.Request(url,headers=headers)

#执行请求获取响应信息
res = urllib.request.urlopen(req)
# 从响应对象中读取信息并解码
html = res.read().decode("utf-8")

#print(len(html))
#使用正则解析出新闻标题信息
dlist = re.findall(pat,html)

content = ''
for v in dlist:
    if isInfo(v[1], v[0]):
        content += (v[1]+":"+v[0]+"\r\n")

with open('data/finance.txt', 'w', encoding='utf-8') as f:
    f.write(content)
	

url = "https://news.sina.com.cn/world/"
#伪装浏览器用户
headers = {'User-Agent':'User-Agent:Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'}
req = urllib.request.Request(url,headers=headers)
###

#执行请求获取响应信息
res = urllib.request.urlopen(req)
# 从响应对象中读取信息并解码
html = res.read().decode("utf-8")

#print(len(html))
#使用正则解析出新闻标题信息
dlist = re.findall(pat,html)

content = ''
for v in dlist:
    if len(v[1]) < 5:
        continue
    if isInfo(v[1], v[0]):
        content += (v[1]+":"+v[0]+"\r\n")

with open('data/world.txt', 'w', encoding='utf-8') as f:
    f.write(content)
