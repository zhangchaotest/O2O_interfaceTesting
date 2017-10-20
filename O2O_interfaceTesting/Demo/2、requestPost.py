#coding=utf-8
import requests
'''

status_code  状态码
headers
raw
url
encoding
history
reason
cookies
elapsed
request
'''
# 单接口访问并显示内容

# 最基本的GET请求
r = requests.get(url='http://www.baidu.com')
print 1, r.url  # 输出一个url http://www.baidu.com/
print 2, r.content  # 输出内容
print 3, r.elapsed  # 输出时间
print 4, r.cookies
print 5, r.encoding
print 6, r.headers
print 7, r.history
print 8, r.links
print 9, r.request
print 10, r.status_code
print 11, r.apparent_encoding
print 12, r.close()
print 13, r.is_permanent_redirect
print 14, r.ok
print 15, r.raw

# 获取返回状态
print(r.request)
# r = requests.get(url='http://dict.baidu.com/s', params={'wd':'python'})
# #带参数的GET请求
# print(r.url)
# #打印解码后的返回数据
# print(r.text)