# 请求网页
import requests
import re
import time
import os

# 反爬
headers = {
    'user-agent': "jinfan is a handsome man!"  # 私有魔法
}

response = requests.get('https://www.vmgirls.com/13506.html', headers=headers)
html = response.text

# 解析网页
urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html)
print(urls)

# 保存图片
output_file = 'images/'
if not os.path.exists(output_file):
    os.mkdir(output_file)
for url in urls:
    time.sleep(0.5)
    filename = output_file + url.split("/")[-1]
    response = requests.get(url, headers=headers)
    with open(filename, 'wb') as f:
        f.write(response.content)



