# -*- coding: utf-8 -*-
import requests

from gs_sign import generateSignGetbx
from utils.tools_print import better_print, error_print
import constants


def get_StudentClass():
    url = "http://gatewaytest.gaosiedu.com/student/api/V2/StudentClass/ClassList"

    params = {
        "classStatus": 1,
        "pageIndex": 1,
        "pageSize": 15,
        "studentCode": constants.StudentCode,
        "wayOfTeaching": -1,
        "xueKe": 0
    }
    sign = generateSignGetbx(params=params, utoken=constants.UToken)
    headers = {
        "Accept": "*/*",
        "partner": "10016",
        "ptoken": constants.PToken,
        "prefreshtoken": constants.PRefreshToken,
        "os": "iOS:13.3.1%20iPhone%206s%20WIFI",
        "winClientVersion": "3.1.0",
        "Accept-Language": "zh-Hans-CN;q=1",
        "uToken": constants.UToken,
        "User-Agent": "gao si jiao yu/3.1.0 (iPhone; iOS 13.3.1; Scale/2.00)",
        "sign": sign
    }

    res = requests.get(url=url, params=params, headers=headers)
    print(res.status_code)
    print(better_print(res.content))
    if res.status_code == 200:
        print(better_print(res.content))
        print(res.text)
    else:
        print(error_print(res.content))


if __name__ == '__main__':
    get_StudentClass()
