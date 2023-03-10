import requests
from bs4 import BeautifulSoup
import re
import json


# 一.采集最近一日世界各国的疫情数据

# 1. 发送请求，获取疫情首页
response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
home_page = response.content.decode()

# 2. 从疫情首页中提取最近一日的各国疫情字符串
soup = BeautifulSoup(home_page, 'lxml')
# print(soup)
script = soup.find(id="getListByCountryTypeService2true")
# print(script)
text = script.get_text
print(text)

# 3. 从最近一日各国的疫情字符串中，提取json格式的字符串
json_str = re.findall('[(.+)]', text)[0]
# [0]--提取为列表

# 4. 把json格式的字符串，转换为Python类型
last_day_corona_virus = json.loads(json_str)

# 5. 以json格式保存，最近一日的各国疫情数据
# 在该项目下建立一个json文件 ，用于存储最近一日的各国疫情信息
with open('venv/last_day_corona_virus.json', 'w') as fp:
    json.dump(last_day_corona_virus, fp, ensure_ascii=False)

