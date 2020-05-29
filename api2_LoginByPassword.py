# -*- coding: utf-8 -*-

import requests

from api1_Salt import get_salt
from gs_sign import passwd_md5, generateSignPost
from utils.tools_print import better_print


def login_by_passwd(phone, password, clientid):
    url = "http://gatewaytest.gaosiedu.com/reg/api/30/Student/LoginByPassword"
    salt = get_salt(name=phone)
    passwd2md5 = passwd_md5(password, salt)
    data = {
        "Phone": phone,
        "Password": passwd2md5,
        "ClientId": clientid
    }
    sign = generateSignPost(data=data)
    headers = {
        "Accept": "*/*",
        "partner": "10016",
        "ptoken": "",
        "os": "iOS:13.3.1%20iPhone%206s%20WIFI",
        "winClientVersion": "3.1.0",
        "Accept-Language": "zh-Hans-CN;q=1",
        "Accept-Encoding": "gzip, deflate",
        "prefreshtoken": "",
        "Content-Type": "application/json",
        "User-Agent": "gao si jiao yu/3.1.0 (iPhone; iOS 13.3.1; Scale/2.00)",
        "sign": sign

    }
    res = requests.post(url=url, json=data, headers=headers)
    print(res.status_code)
    print(better_print(res.content))


if __name__ == '__main__':
    login_by_passwd(phone="13387836885", password="000000", clientid="10000")
