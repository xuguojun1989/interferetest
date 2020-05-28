# -*- coding: utf-8 -*-

import requests

url = "http://gatewaytest.gaosiedu.com/reg/api/30/Student/LoginByPassword"

data = {
    "Phone": "13387836885",
    "Password": "ada830094c2de643a8338da9aec82269",
    "ClientId": "10000"
}
headers = {
    "Accept": "*/*",
    "partner": "10016",
    "ptoken": "",
    "os": "iOS:13.3.1%20iPhone%206s%20WIFI",
    "winClientVersion": "3.1.0",
    "Accept-Language": "zh-Hans-CN;q=1",
    "prefreshtoken":"",
    "User-Agent":"gao si jiao yu/3.1.0 (iPhone; iOS 13.3.1; Scale/2.00)",


}

res = requests.post(url=url, json=data, headers="")
