# -*- coding: utf-8 -*-

import requests

from utils.tools_print import better_print
import constant

host = constant.HOST
api = "/reg/api/v3/SMS/QueryVerificationCode"
# api = "/reg/api/v3/SMS/QueryVerificationCode?phone=18515353986&type=0"
url = host + api
print(url)

# 头部常规参数：
content_type = constant.CONTENT_TYPE1
user_agent = constant.USER_AGENT
# 头部签名参数
usrSign = {
    "13387836887": [constant.SIGN133SMS_0, constant.SIGN133SMS_1, constant.SIGN133SMS_2, constant.SIGN133SMS_3],
    "18515353986": [constant.SIGN185SMS_0, constant.SIGN185SMS_1, constant.SIGN185SMS_2, constant.SIGN185SMS_3]
}
partner = constant.PARTNER
# get请求参数 验证码用途，0：登录，1：修改密码，2：绑定手机号，3：兑换体验卡
type = "0"
# k:手机号，v:[登录签名，修改密码签名]
phone = "18515353986"
sign = usrSign[phone][int(type)]

headers = {
    "sign": sign,
    "partner": partner,
    "content-type": content_type,
    "User-Agent": user_agent
}
params = {
    "phone": phone,
    "type": type

}
res = requests.get(url=url, params=params, headers=headers)
print(better_print(res.content))
# print(better_print(res.text))
# print(res.status_code)
