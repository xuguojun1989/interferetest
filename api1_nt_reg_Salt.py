# -*- coding: utf-8 -*-
import requests

from gs_sign import generateSignGetbx
from utils.tools_print import better_print, error_print


def get_salt(name):
    url = "http://gatewaytest.gaosiedu.com/reg/api/Util/Salt"

    params = {
        "name": name
    }
    sign = generateSignGetbx(params=params)
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
    # print(res.status_code)
    # print(better_print(res.content))
    if res.status_code == 200:
        salt = res.json().get('AppendData').get('Salt')
        # print(salt)
        return salt
    else:
        print(error_print(res.content))


if __name__ == '__main__':
    get_salt(name="13387836885")
