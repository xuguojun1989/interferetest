# -*- coding: utf-8 -*-

import requests

from api1_Salt import get_salt
from gs_sign import passwd_md5, generateSignPost
from utils.tools_print import better_print


def login_by_passwd(phone, password, clientid):
    url = "http://gatewaytest.gaosiedu.com/reg/api/30/Student/LoginByPassword"
    salt = get_salt(phone)
    passwd2md5 = passwd_md5(password, salt)
    data = {
        "Phone": phone,
        "Password": passwd2md5,
        "ClientId": clientid
    }
    print(data)
    sign = generateSignPost(data=data)
    headers = {
        "partner": "10016",
        "winclientversion": "3.1.0",
        "os": "iOS:13.3.1%20iPhone%206s%20WIFI",
        "sign": sign

    }
    print(headers)
    res = requests.post(url=url, json=data, headers=headers)
    print(res.status_code)
    print(better_print(res.content))


if __name__ == '__main__':
    login_by_passwd("18515353986", "000000", "10000")
