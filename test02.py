# -*- coding: utf-8 -*-
from gs_sign import generateSignGetbx

import requests

url = "http://gatewaytest.gaosiedu.com/reg/api/Util/Salt"

params = {
    "name": "13387836885"

}
sign = generateSignGetbx(params=params, bxEvn="gaosiedu", partner="10016")
headers = {
    "Accept": "*/*",
    "partner": "10016",
    "ptoken": "",
    "os": "iOS:13.3.1%20iPhone%206s%20WIFI",
    "winClientVersion": "3.1.0",
    "Accept-Language": "zh-Hans-CN;q=1",
    "prefreshtoken": "",
    "User-Agent": "gao si jiao yu/3.1.0 (iPhone; iOS 13.3.1; Scale/2.00)",
    "sign": sign

}

res = requests.get(url=url, params=params, headers=headers)
print(res.status_code)
print(res.json())
