# 请求网页
import requests
import re
import time
import os

# 反爬
headers = {
    'user-agent': "jinfan is a handsome man!"  # 私有魔法
}

response = requests.get('https://www.vmgirls.com/13821.html', headers=headers)
html = response.text

# 解析网页
urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html)
print(urls)
