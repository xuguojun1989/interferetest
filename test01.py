# -*- coding: utf-8 -*-
import requests

url = "https://www.baidu.com"
res = requests.get(url)
print(res.status_code)
