import requests
import re
from bs4 import BeautifulSoup

response = requests.get('https://www.bilibili.com/')
print(response)
print(response.text)
print(response.content.decode())

html = response.content.decode()
soup = BeautifulSoup(html, 'lxml')
a = soup.find('title')

print(a)

# rs = re.findall(p,s)
rs = re.findall('abc', 'abcfaujegfjhabcdfahabc')
print(rs)
rs = re.findall('a.c', 'aefjiiiabcabfcjafkjfabc')
print(rs)
rs = re.findall('a.c', 'abc')
print(rs)
rs = re.findall('a.c', 'a\nc')
print(rs)
rs = re.findall('a[bc]d', 'abd')
print(rs)
# 匹配数字0~9
rs = re.findall('\d', '1234560')
print(rs)
# 匹配字母数字下划线中文
rs = re.findall('\w', '123')
print(rs)
# 匹配非数字
rs = re.findall('\D', '123')
print(rs)
# 前面的匹配模式出现0次或多次
rs = re.findall('\d*', '123')
print(rs)
# 前面的匹配模式出现1次或多次
rs = re.findall('\d+', '123')
print(rs)
# 前面的匹配模式出现0次或多次
rs = re.findall('a\d*', 'a123456')
print(rs)
# 前面的匹配模式出现0次或1次
rs = re.findall('a\d?', 'a12bc')
print(rs)
# 前面的匹配模式出现指定次数
rs = re.findall('a\d{3}', 'a12453')
print(rs)
rs = re.findall('a,c', 'a\n')
print(rs)
# findall方法中，flag 参数的作用
rs = re.findall('a.c', 'a\nc', re.DOTALL)
print(rs)
rs = re.findall('a.c', 'a\nc', re.S)
print(rs)
# findall方法中分组的使用，分组用于确定位置
rs = re.findall("a(.+)c", 'a\nc')
print(rs)
rs = re.findall('a.+c', 'a\nc', re.DOTALL)
print("1", rs)
rs = re.findall('a(.+)c', 'a\nc', re.DOTALL)
print(rs)
rs = re.findall('a(.+)c', 'a\nc', re.DOTALL)
print(rs)
rs = re.findall('a(.+)c', 'a\n法可覆盖00c', re.DOTALL)
print(rs)

# 正则表达式中使用r原串的作用: 忽略转义符号带来的影响，也可以解决写正则时不符合PEP8的问题

rs = re.findall('a\nbc', 'a\nbc')
print(rs)
rs = re.findall('a\\nbc', 'a\\nbc')
print(rs)
rs = re.findall('a\\\nbc', 'a\\\nbc')
print(rs)
rs = re.findall(r'abc', 'a[]bc')
print(rs)
rs = re.findall(r'a\nbc', 'a\nbc')
print(rs)
rs = re.findall(r'a\\nbc', 'a\\nbc')
print(rs)

a = [{"name": "小妹"}, {"height": 175}, {"weight": 45}]
rs = re.findall('(.*)', a)[0]
print(rs)
