# -*- coding: utf-8 -*-
import json

import requests

from api1_Salt import get_salt
from gs_sign import passwd_md5, generateSignPost
from utils.tools_print import better_print


def login_by_passwd(phone, password, client="10000"):
    url = "http://gatewaytest.gaosiedu.com/reg/api/30/Student/LoginByPassword"
    salt = get_salt(phone)
    passwd2md5 = passwd_md5(passwd=password, salt=salt)
    data = {'Phone': phone, 'Password': passwd2md5, 'ClientId': client}
    print(data)
    sign = generateSignPost(data=data)
    headers = {
        "Host": "gatewaytest.gaosiedu.com",
        "partner": "10016",
        "ptoken": "",
        "os": "iOS:13.3.1%20iPhone%206s%20WIFI",
        "winClientVersion": "3.1.0",
        "Accept-Language": "zh-Hans-CN;q=1",
        "Accept-Encoding": "gzip, deflate",
        "prefreshtoken": "",
        "Content-Type":"application/json",
        "User-Agent": "gao si jiao yu/3.1.0 (iPhone; iOS 13.3.1; Scale/2.00)",
        "sign": sign

    }
    print(headers)
    res = requests.post(url=url, json=data, headers=headers)
    print(res.status_code)
    print(better_print(res.content))


if __name__ == '__main__':
    login_by_passwd("13387836886", "000000")
